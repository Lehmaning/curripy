from typing import Callable, TypeVar, Any

from ..utils import curry, curry_right, partial, tap, identity
from ..operator_.pointfree import pass_arg

__all__ = [
    "print_",
    "globals_",
    "help_",
    "input_",
    "vars_",
    "if_then_else",
    "if_then",
    "if_",
    "then_",
    "else_",
]

# exported functions
hasattr_ = curry_right(hasattr)
print_ = tap(print)
globals_ = tap(globals)
help_ = tap(help)
input_ = tap(input)
vars_ = tap(vars)

__ArgumentType = TypeVar("__ArgumentType")
__ReturnType = TypeVar("__ReturnType")
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
    condition: Callable[[__ArgumentType], bool],
    f: Callable[[__ArgumentType], __ReturnTypeThen],
):
    return if_then_else(condition)(f)(identity)


def if_(condition) -> Callable:
    return partial(if_then_else, condition)


then_ = pass_arg
else_ = pass_arg

# functions which are not exported by default
isinstance_ = curry_right(isinstance, arity=2)
issubclass_ = curry_right(issubclass, arity=2)


@curry
def setattr_(name: str, value: Any) -> Callable[[object], None]:
    return partial(setattr, name, value)


@curry
def getattr_(name: str, default):
    return partial(getattr, name, default=default)
