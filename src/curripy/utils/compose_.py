"""
Attention: This module is not in use. Just written for experiments.
"""

from functools import reduce
from curripy.utils.pass_arg import pass_arg

__all__ = ["pipe"]

def pipe(*funcs):
    if len(funcs) == 1:
        return funcs[0]
    def reducer(instance=None):
        nonlocal funcs
        return reduce(pass_arg, funcs, instance)

    return reducer

def compose(*funcs):
    if len(funcs) == 1:
        return funcs[0]
    def reducer(instance):
        nonlocal funcs
        return reduce(pass_arg, reversed(funcs), instance)

    return reducer
