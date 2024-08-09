from functools import reduce
from .call_ import pass_arg_

__all__ = ["dot", "cdot", "compose", "pipe"]


def cdot(f):
    """
    Same as dot, but curried.
    """

    def __dot(g):
        def caller(x):
            nonlocal f
            nonlocal g
            return g(f(x))

        return caller

    return __dot


def dot(f, g):
    """
    A function that acts lke '.' in Haskell, which does not mean the dot operator between matrices.

    Args:
        f (Callable[[ParamT], ReturnT1]): first function
        g (Callable[[ReturnT1], ReturnT2]): second function

    Returns:
        Callable[[ParamT], ReturnT2]: composed function
    """

    def caller(x):
        nonlocal f
        nonlocal g
        return g(f(x))

    return caller


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
