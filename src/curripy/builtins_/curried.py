from typing import Any, Callable, Iterable, TypeVar

from curripy.utils import curry, partial

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

def filter_(func: Callable[[ParamType], ReturnType] | None):
    return partial(filter, func)

def map_(
    func: Callable[[ParamType], ReturnType],
):
    return partial(map, func)


@curry
def getattr_(o: Any, name: str, default: ReturnType | None = None) -> Any | ReturnType:
    return getattr(o, name, default)


@curry
def setattr_(o: Any, name: str, value: Any) -> None:
    return setattr(o, name, value)
