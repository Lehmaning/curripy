from typing import Callable

from ..functionalize_tools import curry_right

__all__ = [
    "pass_arg",
]


def pass_arg(arg, obj: Callable):
    """Same as obj(*args, **kwargs)."""
    return obj(arg)
