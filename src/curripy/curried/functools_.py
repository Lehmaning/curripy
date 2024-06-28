from functools import reduce
from typing import Callable, Iterable

from returns.curry import curry


@curry
def reduce_(function: Callable, sequence: Iterable):
    return reduce(function, sequence)
