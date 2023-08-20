"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class Server(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    VERSION_FIELD_NUMBER: builtins.int
    name: builtins.str
    version: builtins.str
    def __init__(
        self,
        *,
        name: builtins.str = ...,
        version: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["name", b"name", "version", b"version"]) -> None: ...

global___Server = Server

@typing_extensions.final
class StartRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    BINARY_FIELD_NUMBER: builtins.int
    BINARY_ARGS_FIELD_NUMBER: builtins.int
    AFLPP_ARGS_FIELD_NUMBER: builtins.int
    SEEDS_FIELD_NUMBER: builtins.int
    binary: builtins.bytes
    binary_args: builtins.str
    aflpp_args: builtins.str
    @property
    def seeds(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.bytes]: ...
    def __init__(
        self,
        *,
        binary: builtins.bytes = ...,
        binary_args: builtins.str = ...,
        aflpp_args: builtins.str = ...,
        seeds: collections.abc.Iterable[builtins.bytes] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["aflpp_args", b"aflpp_args", "binary", b"binary", "binary_args", b"binary_args", "seeds", b"seeds"]) -> None: ...

global___StartRequest = StartRequest

@typing_extensions.final
class StartReply(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SUCCESS_FIELD_NUMBER: builtins.int
    success: builtins.bool
    def __init__(
        self,
        *,
        success: builtins.bool = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["success", b"success"]) -> None: ...

global___StartReply = StartReply

@typing_extensions.final
class StopRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___StopRequest = StopRequest

@typing_extensions.final
class StopReply(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SUCCESS_FIELD_NUMBER: builtins.int
    success: builtins.bool
    def __init__(
        self,
        *,
        success: builtins.bool = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["success", b"success"]) -> None: ...

global___StopReply = StopReply
