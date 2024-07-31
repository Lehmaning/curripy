from typing import Callable, TypeVar

from ...functionalize_tools import curry, curry_right, identity, partial, tap
from ..operator_.pointfree import pass_arg


isinstance_ = curry_right(isinstance, arity=2)
issubclass_ = curry_right(issubclass, arity=2)
getattr_ = curry_right(getattr, arity=2)
hasattr_ = curry_right(hasattr)
print_ = tap(print)
globals_ = tap(globals)
help_ = tap(help)
input_ = tap(input)
setattr_ = curry_right(setattr)
vars_ = tap(vars)


__ArgumentType = TypeVar("__ArgumentType")
__ReturnTypeThen = TypeVar("__ReturnTypeThen")
__ReturnTypeElse = TypeVar("__ReturnTypeElse")

@curry
def if_then_else(
    condition: Callable[[__ArgumentType], bool],
    f: Callable[[__ArgumentType], __ReturnTypeThen],
    else_: Callable[[__ArgumentType], __ReturnTypeElse],
    x: __ArgumentType,
):
    return f(x) if condition(x) else else_(x)


@curry
def if_then(
    condition: Callable[[__ArgumentType], bool], f: Callable[[__ArgumentType], __ReturnTypeThen]
):
    return partial(if_then_else, condition, f, identity)


def if_(condition) -> Callable:
    return partial(if_then_else, condition)


then_ = pass_arg
else_ = pass_arg
