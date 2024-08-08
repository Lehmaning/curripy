from .compose_ import pipe, compose, dot, cdot
from .curry_ import curry, curry_right
from .partial_ import partial
from .tap_ import tap
from .cond import if_, if_then, if_then_else, then, else_
from .identity_ import identity
from .call_ import pass_arg, pass_arg_

__all__ = [
    "pipe",
    "compose",
    "cdot",
    "dot",
    "curry",
    "curry_right",
    "partial",
    "tap",
    "if_",
    "if_then",
    "if_then_else",
    "then",
    "else_",
    "identity",
    "pass_arg",
    "pass_arg_",
]
