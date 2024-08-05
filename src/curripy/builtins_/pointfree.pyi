from typing import TypeGuard, overload, Callable, TypeAlias, TypeVar, Annotated
from types import UnionType
import sys

ReturnType = TypeVar("ReturnType")
ParamType = TypeVar("ParamType")

if sys.version_info >= (3, 10):
    _ClassInfo: TypeAlias = type | UnionType | tuple[_ClassInfo, ...]
    """a simulated type to the one with the same name in builtins.pyi"""
else:
    _ClassInfo: TypeAlias = type | tuple[_ClassInfo, ...]
@overload
def isinstance_(
    class_or_tuple: int,
) -> Callable[[object], TypeGuard[int]]: ...
@overload
def isinstance_(
    class_or_tuple: str,
) ->  Callable[[object], TypeGuard[str]]: ...
@overload
def isinstance_(
    class_or_tuple: _ClassInfo,
) -> Callable[[object], bool]:
    def __obj(obj: object) -> bool: ...
    return __obj

def issubclass_(cls: type) -> Callable[[_ClassInfo], bool]: ...
def filter_(func: Callable[[ParamType], ReturnType] | None): ...
def map_(func: Callable[[ParamType], ReturnType] | None): ...
