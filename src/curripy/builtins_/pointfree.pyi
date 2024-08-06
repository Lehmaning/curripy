from typing import TypeGuard, overload, Callable, TypeAlias, TypeVar
from types import UnionType
import sys
from ..__generics import ParamType, ReturnType

__all__ = [
    "hasattr_",
    "print_",
    "help_",
]

if sys.version_info >= (3, 10):
    _ClassInfo: TypeAlias = type | UnionType | tuple[_ClassInfo, ...]
    """a simulated type to the one with the same name in builtins.pyi"""
else:
    _ClassInfo: TypeAlias = type | tuple[_ClassInfo, ...]

@overload
def isinstance_(
    class_or_tuple: type[int],
) -> Callable[[object], TypeGuard[int]]: ...
@overload
def isinstance_(
    class_or_tuple: type[str],
) ->  Callable[[object], TypeGuard[str]]: ...
@overload
def isinstance_(
    class_or_tuple: _ClassInfo,
) -> Callable[[object], bool]:
    def __obj(obj: object) -> bool: ...
    return __obj

def issubclass_(cls: type) -> Callable[[_ClassInfo], bool]: ...
