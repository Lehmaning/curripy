from typing import Any, Callable, TypeVar

from ..utils import curry, partial, map_, filter_

__all__ = [
    "isinstance_",
    "issubclass_",
    "divmod_",
    "getattr_",
    "setattr_",
    "map_",
    "filter_",
    "next_",
]


ReturnType = TypeVar("ReturnType")
ParamType = TypeVar("ParamType")

isinstance_ = curry(isinstance)
issubclass_ = curry(issubclass)
divmod_ = curry(divmod)


def next_(default):
    return partial(next, default)


@curry
def getattr_(o: Any, name: str, default: ReturnType | None = None) -> Any | ReturnType:
    return getattr(o, name, default)


@curry
def setattr_(o: Any, name: str, value: Any) -> None:
    return setattr(o, name, value)
