from uuid import uuid4

from server.output.chat_pb2 import UserInfo


class UserManager:
    _users: [UserInfo]

    def add_user(self, user_name: str) -> UserInfo:
        user = UserInfo(user_name=user_name, uid=str(uuid4()))
        self._users.append(user)
        return user

    def find_user(self, user_name: str) -> UserInfo | None:
        for user in self._users:
            user: UserInfo
            if user.user_name == user_name:
                return user
        return None

    def remove_user(self, user_name: str) -> bool:
        for user in self._users:
            user: UserInfo
            if user.user_name == user_name:
                self._users.remove(user)
                return True
        return False
