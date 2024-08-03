"""
Attention: This module is not in use. Just written for experiments.
"""

from functools import partial
from inspect import getfullargspec
from typing import Callable

from curripy.functionalize_tools.compose import pipe


def get_args(obj: partial):
    return obj.args


get_len_of_args = pipe(getfullargspec, get_args, len)


def curry(function: Callable, arity=None, *args, **kwargs):
    arity = get_len_of_args(function) if arity is None else arity
    args = () if args is None else args
    kwargs = {} if kwargs is None else kwargs
    if len(args) + len(kwargs) >= arity:
        return function(*args, **kwargs)

    def caller(*passing_args, **passing_kwargs):
        nonlocal args
        nonlocal kwargs
        nonlocal function
        args = args + passing_args
        kwargs = kwargs | passing_kwargs
        return curry(function, arity, *args, **kwargs)

    return caller
