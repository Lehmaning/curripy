from ..utils.partial_ import partial
from ..utils.curry_ import curry
from .pass_arg import pass_arg
from ..utils.identity_ import identity

__all__ = ["if_then_else", "if_then", "if_", "then", "else_"]

def if_then_else_(
    cond,
    f,
    else_,
    x,
):
    return f(x) if cond(x) else else_(x)


if_then_else = curry(if_then_else_)


def if_then_(
    cond,
    f,
):
    return partial(if_then_else_, cond, f, identity)
if_then = curry(if_then_)

def if_(cond):
    return if_then_else(cond)
then = pass_arg
else_ = pass_arg
