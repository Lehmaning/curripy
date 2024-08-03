from typing import Iterable, Any, Callable, TypeVar

from returns.curry import curry, partial

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


__ReturnType = TypeVar("__ReturnType")
__ArgumentType = TypeVar("__ArgumentType")

isinstance_ = curry(isinstance)
issubclass_ = curry(issubclass)
divmod_ = curry(divmod)


def next_(default):
    return partial(next, default)


def filter_(function: Callable | None):
    return partial(filter, function)


def map_(
    function: Callable[[__ArgumentType], __ReturnType],
) -> Callable[[Iterable[__ArgumentType]], map]:
    return partial(map, function)


@curry
def getattr_(o: Any, name: str, default: __ReturnType = None) -> Any | __ReturnType:
    return getattr(o, name, default)


@curry
def setattr_(o: Any, name: str, value: Any) -> None:
    return setattr(o, name, value)
