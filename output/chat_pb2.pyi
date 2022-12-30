from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ChatRequest(_message.Message):
    __slots__ = ["message", "sender"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    SENDER_FIELD_NUMBER: _ClassVar[int]
    message: str
    sender: UserInfo
    def __init__(self, sender: _Optional[_Union[UserInfo, _Mapping]] = ..., message: _Optional[str] = ...) -> None: ...

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

class ListenRequest(_message.Message):
    __slots__ = ["me"]
    ME_FIELD_NUMBER: _ClassVar[int]
    me: UserInfo
    def __init__(self, me: _Optional[_Union[UserInfo, _Mapping]] = ...) -> None: ...

class UserInfo(_message.Message):
    __slots__ = ["random_color", "user_name"]
    RANDOM_COLOR_FIELD_NUMBER: _ClassVar[int]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    random_color: str
    user_name: str
    def __init__(self, user_name: _Optional[str] = ..., random_color: _Optional[str] = ...) -> None: ...
