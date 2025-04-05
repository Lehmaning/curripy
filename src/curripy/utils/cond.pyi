from typing import Callable, TypeVar

from curripy._bootstrap.identity import identity

from curripy.__generics import ParamT
from .curry import curry

ReturnThen = TypeVar("ReturnThen")
ReturnElse = TypeVar("ReturnElse")

__all__ = (
    "if_then_else",
    "if_then",
    "if_then_else_",
    "if_then_",
    "if_",
    "then",
    "else_",
)

def if_then_else_(
    c: Callable[[ParamT], bool],
    f: Callable[[ParamT], ReturnThen],
    e: Callable[[ParamT], ReturnElse],
    x: ParamT,
) -> ReturnThen | ReturnElse: ...
def if_then_(
    c: Callable[[ParamT], bool],
    f: Callable[[ParamT], ReturnThen],
) -> Callable[[ParamT], ReturnThen | ParamT]: ...

if_then_else = curry(if_then_else_, arity=4)
if_then = curry(if_then_, arity=2)

def cond(
    c: Callable[[ParamT], bool],
    f: Callable[[ParamT], ReturnThen],
    e: Callable[[ParamT], ReturnElse],
) -> Callable[[ParamT], ReturnThen | ReturnElse]:
    """This function uses dummy typing for directly mark the type of the return function.

    Args:
        c (Callable[[ParamT], bool]): condition
        f (Callable[[ParamT], ReturnThen]): then
        e (Callable[[ParamT], ReturnElse]): else

    Returns:
        Callable[[ParamT], ReturnThen | ReturnElse]: result function
    """
    ...

if_ = identity
then = identity
else_ = identity
