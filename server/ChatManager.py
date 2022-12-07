from asyncio import Event

from server.output.chat_pb2 import ChatRequest, UserInfo


class ChatManager:
    def __init__(self):
        self.event = Event()
        self.undeployed_chats: [ChatRequest] = []

    def get_first_undeployed_chat(self) -> ChatRequest | None:
        if self.undeployed_chats:
            return self.undeployed_chats.pop(0)
        else:
            return None

    # def get_latest_chat(self, my_name: str, sender_name: str) -> ChatRequest:
    #     chats: [Chat] = c.get_chats(target_name=my_name, sender_name=sender_name)
    #     for chat in chats:
    #         chat: Chat
    #         if chat.file_id is not None:
    #             return ChatRequest(
    #                 sender=UserInfo(user_name=chat.sender_name),
    #                 file=f.get_file_by_id(chat.file_id)
    #             )
    #         else:
    #             return ChatRequest(
    #                 sender=UserInfo(user_name=chat.sender_name),
    #                 message=chat.message
    #             )

    # def get_all_chats(self, my_name: str, sender_name: str | None = None) -> [ChatRequest]:
    #     chats = c.get_chats(target_name=my_name, sender_name=sender_name)
    #     results = []
    #     for chat in chats:
    #         chat: Chat
    #         if chat.file_id is not None:
    #             cr = ChatRequest(
    #                 sender=UserInfo(user_name=chat.sender_name),
    #                 file=f.get_file_by_id(chat.file_id)
    #             )
    #         else:
    #             cr = ChatRequest(
    #                 sender=UserInfo(user_name=chat.sender_name),
    #                 message=chat.message
    #             )
    #
    #         results.append(cr)
    #     return results

    def add_chat(self, chat: ChatRequest):
        # c.create_chat(sender_name, target_name, message, file_id)
        self.undeployed_chats.append(chat)
