from .curry import curry
from .identity import identity
from .partial import partial

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


def cond(c, f, e):
    return partial(if_then_else_, c, f, e)


if_then_else = curry(if_then_else_, arity=4)
if_then = curry(if_then_, arity=2)
if_ = identity
then = identity
else_ = identity
