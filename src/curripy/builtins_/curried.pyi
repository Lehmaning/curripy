from typing import Iterable, Iterable, TypeGuard, overload, Callable, TypeAlias, TypeVar
from types import UnionType
from typing_extensions import TypeIs
import sys
from ..utils import curry, partial
from ..__generics import ParamType2, ParamType1, ParamType

if sys.version_info >= (3, 10):
    _ClassInfo: TypeAlias = type | UnionType | tuple[_ClassInfo, ...]
    """a simulated type to the one with the same name in builtins.pyi"""
else:
    _ClassInfo: TypeAlias = type | tuple[_ClassInfo, ...]

def isinstance_(obj: object) -> Callable[[_ClassInfo], TypeIs[_ClassInfo]]: ...
def issubclass_(cls: type) -> Callable[[_ClassInfo], TypeIs[_ClassInfo]]: ...
