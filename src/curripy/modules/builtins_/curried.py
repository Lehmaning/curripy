from typing import Callable

from returns.curry import curry, partial

isinstance_ = curry(isinstance)
issubclass_ = curry(issubclass)
divmod_ = curry(divmod)

@curry
def map_(function: Callable):
    return partial(map, function)

@curry
def filter_(function: Callable | None):
    return partial(filter, function)

@curry
def next_(default):
    return partial(next, default)