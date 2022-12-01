from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ChatRequest(_message.Message):
    __slots__ = ["file", "message", "sender", "target"]
    FILE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    SENDER_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    file: File
    message: str
    sender: UserInfo
    target: UserInfo
    def __init__(self, sender: _Optional[_Union[UserInfo, _Mapping]] = ..., message: _Optional[str] = ..., file: _Optional[_Union[File, _Mapping]] = ..., target: _Optional[_Union[UserInfo, _Mapping]] = ...) -> None: ...

class ChatResponse(_message.Message):
    __slots__ = ["chat_req", "error_message", "success"]
    CHAT_REQ_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    chat_req: ChatRequest
    error_message: str
    success: bool
    def __init__(self, success: bool = ..., chat_req: _Optional[_Union[ChatRequest, _Mapping]] = ..., error_message: _Optional[str] = ...) -> None: ...

class ConnectServerReqeust(_message.Message):
    __slots__ = ["user_name"]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    user_name: str
    def __init__(self, user_name: _Optional[str] = ...) -> None: ...

class ConnectServerResponse(_message.Message):
    __slots__ = ["error_message", "success", "user"]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    error_message: str
    success: bool
    user: UserInfo
    def __init__(self, success: bool = ..., user: _Optional[_Union[UserInfo, _Mapping]] = ..., error_message: _Optional[str] = ...) -> None: ...

class Empty(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class File(_message.Message):
    __slots__ = ["content", "extension", "file_name"]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    EXTENSION_FIELD_NUMBER: _ClassVar[int]
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    content: bytes
    extension: str
    file_name: str
    def __init__(self, content: _Optional[bytes] = ..., extension: _Optional[str] = ..., file_name: _Optional[str] = ...) -> None: ...

class GetAllChatsResponse(_message.Message):
    __slots__ = ["chats"]
    CHATS_FIELD_NUMBER: _ClassVar[int]
    chats: _containers.RepeatedCompositeFieldContainer[ChatRequest]
    def __init__(self, chats: _Optional[_Iterable[_Union[ChatRequest, _Mapping]]] = ...) -> None: ...

class ListenRequest(_message.Message):
    __slots__ = ["me", "sender"]
    ME_FIELD_NUMBER: _ClassVar[int]
    SENDER_FIELD_NUMBER: _ClassVar[int]
    me: UserInfo
    sender: UserInfo
    def __init__(self, me: _Optional[_Union[UserInfo, _Mapping]] = ..., sender: _Optional[_Union[UserInfo, _Mapping]] = ...) -> None: ...

class UserInfo(_message.Message):
    __slots__ = ["user_name"]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    user_name: str
    def __init__(self, user_name: _Optional[str] = ...) -> None: ...

class UserListQueryRequest(_message.Message):
    __slots__ = ["specific_user_name"]
    SPECIFIC_USER_NAME_FIELD_NUMBER: _ClassVar[int]
    specific_user_name: str
    def __init__(self, specific_user_name: _Optional[str] = ...) -> None: ...

class UserListQueryResponse(_message.Message):
    __slots__ = ["error_message", "success", "users"]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    USERS_FIELD_NUMBER: _ClassVar[int]
    error_message: str
    success: bool
    users: _containers.RepeatedCompositeFieldContainer[UserInfo]
    def __init__(self, success: bool = ..., users: _Optional[_Iterable[_Union[UserInfo, _Mapping]]] = ..., error_message: _Optional[str] = ...) -> None: ...
