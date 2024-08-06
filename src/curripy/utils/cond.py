from .call_ import pass_arg
from .curry_ import curry
from .identity_ import identity
from .partial_ import partial

__all__ = ["if_then_else", "if_then", "if_", "then", "else_"]


def if_then_else_(
    c,
    f,
    e,
    x,
):
    return f(x) if c(x) else e(x)


def if_then_(
    c,
    f,
):
    return partial(if_then_else_, c, f, identity)


if_then_else = curry(if_then_else_)
if_then = curry(if_then_)
if_ = if_then_else
then = pass_arg
else_ = pass_arg
