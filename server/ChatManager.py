from asyncio import Event

from sqlalchemy import create_engine

from server.database import chat as c
from server.database import file as f
from server.database.chat import Chat
from server.output.chat_pb2 import ChatRequest, UserInfo


class ChatManager:
    def __init__(self):
        self.event = Event()
        self.engine = create_engine("sqlite://", echo=True, future=True)
        self._temp_undeployed_chats: [ChatRequest] = []

    def get_tuc(self) -> ChatRequest | None:
        if self._temp_undeployed_chats:
            return self._temp_undeployed_chats.pop(0)
        else:
            return None

    def get_latest_chat(self, my_name: str, sender_name: str) -> ChatRequest:
        chats: [Chat] = c.get_chats(target_name=my_name, sender_name=sender_name)
        for chat in chats:
            chat: Chat
            if chat.file_id is not None:
                return ChatRequest(
                    sender=UserInfo(user_name=chat.sender_name),
                    file=f.get_file_by_id(chat.file_id)
                )
            else:
                return ChatRequest(
                    sender=UserInfo(user_name=chat.sender_name),
                    message=chat.message
                )

    def get_all_chats(self, my_name: str, sender_name: str | None = None) -> [ChatRequest]:
        chats = c.get_chats(target_name=my_name, sender_name=sender_name)
        results = []
        for chat in chats:
            chat: Chat
            if chat.file_id is not None:
                cr = ChatRequest(
                    sender=UserInfo(user_name=chat.sender_name),
                    file=f.get_file_by_id(chat.file_id)
                )
            else:
                cr = ChatRequest(
                    sender=UserInfo(user_name=chat.sender_name),
                    message=chat.message
                )

            results.append(cr)
        return results

    def add_chat(self, sender_name: str, target_name: str, message: str | None = None, file_id: int | None = None):
        c.create_chat(sender_name, target_name, message, file_id)
