from functools import partialmethod  # noqa: F401
from operator import attrgetter, methodcaller  # noqa: F401

from .compose_ import pipe
from .builtins_ import map_, filter_
from .curry_ import curry, curry_right
from .partial_ import partial
from .tap_ import tap
from .cond import if_, if_then, if_then_else, then, else_
from .identity_ import identity
from .call_ import pass_arg, pass_arg_