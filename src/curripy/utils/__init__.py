from functools import partialmethod  # noqa: F401
from operator import attrgetter, methodcaller  # noqa: F401

from .compose_ import pipe
from .curry_ import curry, curry_right
from .partial_ import partial
from .tap_ import tap
from .cond import if_then_else, if_then, if_, else_
from .identity_ import identity