from typing import Literal, overload, TypeVar, Callable
from functools import partial
from ..__generics import ParamType
from .curry_ import curry
from .call_ import pass_arg

__all__ = [
    "if_then_else",
    "if_then",
    "if_then_else_",
    "if_then_",
    "if_",
    "then",
    "else_",
]

ReturnTypeThen = TypeVar("ReturnTypeThen")
ReturnTypeElse = TypeVar("ReturnTypeElse")

def if_then_else_(
    c: Callable[[ParamType], bool],
    f: Callable[[ParamType], ReturnTypeThen],
    e: Callable[[ParamType], ReturnTypeElse],
    x: ParamType,
) -> ReturnTypeThen | ReturnTypeElse: ...
def if_then_(
    c: Callable[[ParamType], bool],
    f: Callable[[ParamType], ReturnTypeThen],
) -> Callable[[ParamType], ReturnTypeThen | ParamType]: ...

if_then_else = curry(if_then_else_)
if_then = curry(if_then_)
if_ = if_then_else
then = pass_arg
else_ = pass_arg
