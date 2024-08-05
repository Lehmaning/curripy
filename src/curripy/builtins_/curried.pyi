from typing import TypeGuard, overload, Callable, TypeAlias, TypeVar
from types import UnionType
import sys

ReturnType = TypeVar("ReturnType")
ParamType = TypeVar("ParamType")

if sys.version_info >= (3, 10):
    _ClassInfo: TypeAlias = type | UnionType | tuple[_ClassInfo, ...]
    """a simulated type to the one with the same name in builtins.pyi"""
else:
    _ClassInfo: TypeAlias = type | tuple[_ClassInfo, ...]

def isinstance_(
    obj: object,
) -> Callable[[_ClassInfo], bool]:
    def class_or_tuple(class_or_tuple: _ClassInfo) -> bool: ...
    return class_or_tuple

def issubclass_(cls: type) -> Callable[[_ClassInfo], bool]: ...
def filter_(func: Callable[[ParamType], ReturnType] | None): ...
def map_(func: Callable[[ParamType], ReturnType] | None): ...
