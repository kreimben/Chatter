from typing import AsyncGenerator

from server.ChatManager import ChatManager
from server.UserManager import UserManager
from server.database.file import create_file
from server.output import chat_pb2_grpc
from server.output.chat_pb2 import ConnectServerReqeust, ConnectServerResponse, ChatRequest, Empty, ListenRequest, \
    UserListQueryRequest, UserListQueryResponse, GetAllChatsResponse, ChatResponse, UserInfo


class ChattingServicer(chat_pb2_grpc.ChattingServicer):
    def __init__(self, user_manager: UserManager, chat_manager: ChatManager):
        self._user_manager = user_manager
        self._chat_manager = chat_manager
        self._current_users: [UserInfo] = []  # Caution! I can not check which clients currently connected!

    async def ConnectServer(self, request: ConnectServerReqeust, context) -> ConnectServerResponse:
        if self._user_manager.find_user(request.user_name):
            msg = f'Requested name({request.user_name}) has already taken!'
            return ConnectServerResponse(success=False, error_message=msg)
        else:
            user = self._user_manager.add_user(request.user_name)
        return ConnectServerResponse(success=True, user=user)

    async def ListenChat(self, request: ListenRequest, context) -> AsyncGenerator:
        """Listen chat streams.
        """
        while True:
            # Event Loop related code before get datas.
            self._chat_manager.event.clear()

            # chat: ChatRequest = self._chat_manager.get_latest_chat(
            #     my_name=request.me.user_name,
            #     sender_name=request.sender.user_name
            # )
            chat: ChatRequest = self._chat_manager.get_tuc()
            print(f'ListenChat pop_first_chat ({chat is not None}) {chat=}')
            if chat is not None:
                print(f'{chat=} {type(chat)}')
                yield ChatResponse(success=True, chat_req=chat)
                print('+-----------ListenChat End-----------+')
            else:
                print(f'No chat to delivery to client! {chat=}')
                print('+-----------ListenChat End-----------+')
                await self._chat_manager.event.wait()

    async def SendChat(self, request: ChatRequest, context):
        """Broadcast chats.
        """
        print(f'+--------------SendChat Start--------------+')
        if request.file is not None and request.message is None:
            file_obj = create_file(request.file.file_name, request.file.extension, file_content=request.file.content)
            self._chat_manager.add_chat(
                sender_name=request.sender.user_name,
                target_name=request.target.user_name,
                file_id=file_obj
            )
        elif request.file is None and request.message is not None:
            self._chat_manager.add_chat(
                sender_name=request.sender.user_name,
                target_name=request.target.user_name,
                message=request.message
            )
        else:
            print(f'########################################')
            print(f'\tThere is an error!')
            print(f'\tmessage and file exists in same time.')
            print(f'\tmessage: {request.message}')
            print(f'\tfile: {request.file}')
            print(f'########################################')

        return Empty()

    async def GetUserList(self, request: UserListQueryRequest, context) -> UserListQueryResponse:
        return UserListQueryResponse(success=True, users=self._current_users)

    def GetAllChats(self, request: ListenRequest, context) -> GetAllChatsResponse:
        chats: [ChatRequest] = self._chat_manager.get_all_chats(
            my_name=request.me.user_name,
            sender_name=request.sender.user_name
        )

        return GetAllChatsResponse(chats=chats)
