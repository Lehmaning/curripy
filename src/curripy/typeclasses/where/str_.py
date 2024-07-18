from operator import methodcaller as m
from typing import AnyStr, Callable, LiteralString, SupportsIndex, TypeVar

from curripy.typeclasses.class_ import Encodable, Splitable, Strippable

T = TypeVar("T")


def encode(
    encoding: str = "utf-8", errors: str = "strict"
) -> Callable[[Encodable], bytes]:
    return m("encode", encoding, errors)


def split(
    sep: AnyStr, maxsplit: SupportsIndex = -1
) -> Callable[[Splitable], Splitable]:
    return m("split", sep, maxsplit)


def strip(
    chars: str | LiteralString | None = None,
) -> Callable[[Strippable], Strippable]:
    return m("strip", chars)
