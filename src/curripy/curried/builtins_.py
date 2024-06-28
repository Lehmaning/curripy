from typing import Callable, Iterable

from returns.curry import curry


@curry
def map_(func: Callable, iterables: Iterable):
    return map(func, iterables)


@curry
def filter_(function: Callable | None, iterable: Iterable):
    return filter(function, iterable)


@curry
def range_(*args):
    return range(*args)
