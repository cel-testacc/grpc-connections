from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BookDetailsData(_message.Message):
    __slots__ = ["author", "quotes", "title"]
    AUTHOR_FIELD_NUMBER: _ClassVar[int]
    QUOTES_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    author: str
    quotes: str
    title: str
    def __init__(self, author: _Optional[str] = ..., title: _Optional[str] = ..., quotes: _Optional[str] = ...) -> None: ...

class BookDetailsRequest(_message.Message):
    __slots__ = ["author"]
    AUTHOR_FIELD_NUMBER: _ClassVar[int]
    author: str
    def __init__(self, author: _Optional[str] = ...) -> None: ...

class BookDetailsResponse(_message.Message):
    __slots__ = ["bookDetails"]
    BOOKDETAILS_FIELD_NUMBER: _ClassVar[int]
    bookDetails: _containers.RepeatedCompositeFieldContainer[BookDetailsData]
    def __init__(self, bookDetails: _Optional[_Iterable[_Union[BookDetailsData, _Mapping]]] = ...) -> None: ...
