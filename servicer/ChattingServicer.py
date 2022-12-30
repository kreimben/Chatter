import random
from typing import AsyncGenerator

from ChatManager import ChatManager
from output import chat_pb2_grpc
from output import ConnectServerReqeust, ConnectServerResponse, ChatRequest, Empty, ListenRequest, \
    ChatResponse, UserInfo


def get_random_color() -> str:
    r = lambda: random.randint(0, 255)
    return '#%02X%02X%02X' % (r(), r(), r())


class ChattingServicer(chat_pb2_grpc.ChattingServicer):
    def __init__(self, chat_manager: ChatManager):
        self._chat_manager = chat_manager

    async def ConnectServer(self, request: ConnectServerReqeust, context) -> ConnectServerResponse:
        user = UserInfo(user_name=request.user_name, random_color=get_random_color())
        return ConnectServerResponse(success=True, user=user)

    async def ListenChat(self, request: ListenRequest, context) -> AsyncGenerator:
        """Listen chat streams.
        """
        while True:
            # Event Loop related code before get datas.
            self._chat_manager.event.clear()
            chat: ChatRequest = self._chat_manager.get_first_undeployed_chat()
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
        if request.message is not None:
            self._chat_manager.add_chat(request)
        else:
            print(f'########################################')
            print(f'\tThere is an error!')
            print(f'\tmessage and file exists in same time.')
            print(f'\tmessage: {request.message}')
            print(f'########################################')

        return Empty()
