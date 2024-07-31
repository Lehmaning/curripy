from functools import partialmethod, partial, reduce as reduce_
from typing import Callable, Iterable
from operator import attrgetter
from returns.curry import curry


get_partial_func: Callable[[partial | partialmethod], Callable] = attrgetter("func")
get_partial_args: Callable[[partial | partialmethod], Iterable] = attrgetter("args")
get_partial_keywords: Callable[[partial | partialmethod], Iterable] = attrgetter(
    "keywords"
)


@curry
def reduce(function: Callable, sequence: Iterable):
    return reduce_(function, sequence)
