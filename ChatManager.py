from asyncio import Event

from output.chat_pb2 import ChatRequest


class ChatManager:
    def __init__(self):
        self.event = Event()
        self.undeployed_chats: [ChatRequest] = []

    def get_first_undeployed_chat(self) -> ChatRequest | None:
        if self.undeployed_chats:
            return self.undeployed_chats.pop(0)
        else:
            return None

    def add_chat(self, chat: ChatRequest):
        # c.create_chat(sender_name, target_name, message, file_id)
        self.undeployed_chats.append(chat)
