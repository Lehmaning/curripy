from .call_ import pass_arg, pass_arg_
from .compose_ import cdot, compose, dot, pipe
from .cond import else_, if_, if_then, if_then_else, then
from .curry_ import curry, curry_right
from .identity_ import identity
from .partial_ import partial
from .return__ import return_
from .tap_ import tap

__all__ = (
    # from compose
    "pipe",
    "compose",
    "cdot",
    "dot",
    # from curry
    "curry",
    "curry_right",
    # from cond
    "if_",
    "then",
    "else_",
    "if_then",
    "if_then_else",
    # misc
    "identity",
    "partial",
    "tap",
    "pass_arg",
    "pass_arg_",
    "return_",
)
