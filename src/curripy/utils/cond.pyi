from typing import TypeAlias, TypeVar, Callable
from ..__generics import ParamType, ReturnType1, ReturnType2

ReturnTypeThen: TypeAlias = ReturnType1
ReturnTypeElse: TypeAlias = ReturnType2
def if_then_else(
    condition: Callable[[ParamType], bool],
    f: Callable[[ParamType], ReturnTypeThen],
    else_: Callable[[ParamType], ReturnTypeElse],
    x: ParamType,
) -> ReturnTypeThen | ReturnTypeElse: ...

def if_then(
    condition: Callable[[ParamType], bool],
    f: Callable[[ParamType], ReturnTypeThen],
) -> Callable[[ParamType], ParamType | ReturnTypeThen]: ...

def if_(condition: Callable[[ParamType], bool]): ...
def else_(condition: Callable[[ParamType], bool]): ...
def then(f: Callable[[ParamType], ReturnTypeThen]) -> Callable: ...