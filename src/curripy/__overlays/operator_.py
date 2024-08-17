"""
Some functions of operator with better type hints
"""

from operator import is_, is_not, add, sub, rshift, lshift, contains

__all__ = (
    "is_",
    "is_not",
    "add",
    "sub",
    "contains",
    "rshift",
    "lshift",
    # new functions
    "radd",
    "rsub",
    "itemgetter",
    "methodcaller",
    "attrgetter"
)


def radd(a, b):
    return b + a


def rsub(a, b):
    return b - a


def attrgetter(name: str):
    def caller(obj):
        nonlocal name
        return getattr(obj, name)

    return caller


def methodcaller(name: str, *args, **kwargs):
    def caller(obj):
        nonlocal args, kwargs, name
        return getattr(obj, name)(*args, **kwargs)

    return caller


def itemgetter(a):
    def __b(b):
        nonlocal a
        return b[a]

    return __b
