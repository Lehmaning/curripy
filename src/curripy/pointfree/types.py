from ast import TypeVar
from re import Pattern
from typing import (
    Any,
    AnyStr,
    Iterable,
    Iterator,
    LiteralString,
    Protocol,
    Self,
    SupportsIndex,
    overload,
)

T = TypeVar("T")


class Encodable(Protocol):
    def encode(self, encoding: str, errors: str) -> bytes: ...


class Strippable(Protocol):
    def strip(self, sep: LiteralString | str | None) -> Self: ...


class Splitable(Protocol):
    @overload
    def split(
        self: Pattern[str],
        string: str,
        maxsplit: int = 0
    ) -> list[str | Any]: ...
    @overload
    def split(
        self: Pattern[bytes],
        string: Any,
        maxsplit: int = 0
    ) -> list[bytes | Any]: ...
    @overload
    def split(
        self: LiteralString,
        sep: LiteralString | None = None,
        maxsplit: SupportsIndex = -1,
    ) -> list[LiteralString]: ...
    def split(self, *args, **kwargs) -> Any: ...


class Searchable(Protocol):
    def search(self, *args, **kwargs) -> Any | None: ...


class Findallable(Protocol):
    def findall(self, *args, **kwargs) -> Iterable[Self]: ...


class Finditerable(Protocol):
    def findall(self, *args, **kwargs) -> Iterator: ...
