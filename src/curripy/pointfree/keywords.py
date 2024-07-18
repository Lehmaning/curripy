from typing import Callable, Type, TypeVar

from ..functionalize_tools import curry, identity, partial, pipe
from .operator_ import pass_arg

T = TypeVar("T")
U = TypeVar("U")
S = TypeVar("S")


@curry
def if_then_else(
    condition: Callable[[T], bool],
    f: Callable[[T], U],
    else_: Callable[[T], S],
    x: T,
):
    return f(x) if condition(x) else else_(x)


@curry
def if_then(
    condition: Callable[[T], bool], f: Callable[[T], U]
) -> Callable[[T], U | T]:
    return partial(if_then_else, condition, f, identity)


@curry
def if_(condition):
    return if_then_else(condition)

then_ = pass_arg
else_ = then_

if __name__ == "__main__":
    from ..curried.operator_ import eq
    cond = pipe(if_(eq(2)), then_(print), else_(pipe(chr, print)))
    print(cond(114514))