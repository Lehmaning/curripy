from functools import partialmethod  # noqa: F401
from operator import attrgetter, methodcaller  # noqa: F401

from pydash import (
    curry,  # noqa: F401
    curry_right,  # noqa: F401
)
from pydash import flow as pipe_  # noqa: F401
from returns.curry import curry as curry_  # noqa: F401
from returns.curry import partial
from returns.functions import identity, tap  # noqa: F401
from returns.pipeline import pipe  # noqa: F401
