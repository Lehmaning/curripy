"""
Attention: This module is not in use. Just written for experiments.
"""

from typing import Callable, Iterable
from functools import reduce


def pass_arg(arg, obj: Callable):
    return obj(arg)


__initial_missing = object()


def reduce_generator(function, sequence: Iterable, initial=__initial_missing):
    """
    reduce(function, iterable[, initial]) -> value

    Apply a function of two arguments cumulatively to the items of a sequence
    or iterable, from left to right, so as to reduce the iterable to a single
    value.  For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates
    ((((1+2)+3)+4)+5).  If initial is present, it is placed before the items
    of the iterable in the calculation, and serves as a default when the
    iterable is empty.
    """
    it = iter(sequence)
    try:
        value = next(it) if initial is __initial_missing else initial
    except StopIteration:
        raise TypeError("reduce() of empty iterable with no initial value") from None
    else:
        for element in it:
            value = function(value, element)
            yield value


def pipe(*functions):
    def reducer(instance):
        return reduce(pass_arg, functions, instance)

    return reducer


def pipe_generator(*functions):
    def reducer(instance):
        return reduce_generator(pass_arg, functions, instance)

    return reducer
