"""
Attention: This module is not in use. Just written for experiments.
"""

from functools import reduce
from .call_ import pass_arg_

__all__ = ["pipe", "compose"]

def pipe(*funcs):
    if len(funcs) == 1:
        return funcs[0]
    def reducer(instance=None):
        nonlocal funcs
        return reduce(pass_arg_, funcs, instance)

    return reducer

def compose(*funcs):
    if len(funcs) == 1:
        return funcs[0]
    def reducer(instance):
        nonlocal funcs
        return reduce(pass_arg_, reversed(funcs), instance)

    return reducer
