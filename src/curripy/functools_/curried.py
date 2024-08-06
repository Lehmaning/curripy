from functools import reduce as reduce_
from typing import Callable, Iterable
from ..utils import curry

__all__ = [
    "reduce",
]


@curry
def reduce(function: Callable, sequence: Iterable):
    return reduce_(function, sequence)
