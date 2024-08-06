from ..utils import curry_right, tap, curry
from ..__generics import ReturnType
from typing import overload, Callable, Any

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

def setattr_(name: str) -> Callable[[Any], Callable[[object], None]]: ...
def getattr_(name: str, default: ReturnType) -> Callable[[object], ReturnType]: ...
