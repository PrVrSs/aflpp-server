from typing import ClassVar as _ClassVar
from typing import Optional as _Optional

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message


DESCRIPTOR: _descriptor.FileDescriptor

class StartRequest(_message.Message):
    __slots__ = ["filename", "binary", "binary_args"]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    BINARY_FIELD_NUMBER: _ClassVar[int]
    BINARY_ARGS_FIELD_NUMBER: _ClassVar[int]
    filename: str
    binary: bytes
    binary_args: str
    def __init__(self, filename: _Optional[str] = ..., binary: _Optional[bytes] = ..., binary_args: _Optional[str] = ...) -> None: ...

class StartReply(_message.Message):
    __slots__ = ["success"]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    def __init__(self, success: bool = ...) -> None: ...

class StopRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class StopReply(_message.Message):
    __slots__ = ["success"]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    def __init__(self, success: bool = ...) -> None: ...
