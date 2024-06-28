# %%
from operator import methodcaller as m
from typing import Any, AnyStr, Callable, List, LiteralString, SupportsIndex, TypeVar

from curripy.curried.builtins_ import map_
from curripy.pointfree.types import Encodable, Splitable, Strippable
from returns.pipeline import pipe
T = TypeVar("T")


def encode(
    encoding: str = "utf-8", errors: str = "strict"
) -> Callable[[Encodable], bytes]:
    return m("encode", encoding, errors)


def split(sep: AnyStr, maxsplit: SupportsIndex = -1) -> Callable[[Splitable], Splitable]:
    return m("split", sep, maxsplit)


def strip(
    chars: str | LiteralString | None = None,
) -> Callable[[Strippable], Strippable]:
    return m("strip", chars)
