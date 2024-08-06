from ..utils import curry, curry_right, partial, tap

__all__ = [
    "hasattr_",
    "print_",
    "help_",
]

# exported functions
hasattr_ = curry_right(hasattr)
print_ = tap(print)
help_ = tap(help)

# functions which are not exported by default
isinstance_ = curry_right(isinstance, arity=2)
issubclass_ = curry_right(issubclass, arity=2)


@curry
def setattr_(name: str, value):
    return partial(setattr, name, value)


@curry
def getattr_(name: str, default = None):
    return partial(getattr, name, default=default)
