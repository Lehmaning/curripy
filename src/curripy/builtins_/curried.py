from ..utils import curry
from ..__bootstrap.builtins_ import map_, filter_

__all__ = (
    "divmod_",
    "map_",
    "filter_",
)

isinstance_ = curry(isinstance)
issubclass_ = curry(issubclass)
divmod_ = curry(divmod)


# Belows are not exported to the root package by default
@curry
def getattr_(o, name, default=None):
    return getattr(o, name, default)


@curry
def setattr_(o, name, value):
    return setattr(o, name, value)
