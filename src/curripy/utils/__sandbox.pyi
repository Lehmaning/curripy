"""
This module is used for code refactoring or experiments on new feature.
"""

from ..__generics import (
    ParamType1,
    ParamType2,
    ParamType3,
    ParamType4,
    ParamType5,
    ReturnType,
)
from typing import (
    Optional,
    overload,
    Callable,
    ParamSpec,
    TypeVar,
)

@overload
def curry(
    func: Callable[[ParamType1], ReturnType],
    arity: Optional[int] = None,
    **__kwargs,
) -> Callable[[ParamType1], ReturnType]: ...
@overload
def curry(
    func: Callable[[ParamType1, ParamType2], ReturnType],
    arg: ParamType1,
    arity: Optional[int] = None,
    **__kwargs,
) -> Callable[[ParamType2], ReturnType]: ...
@overload
def curry(
    func: Callable[[ParamType1, ParamType2, ParamType3], ReturnType],
    arg: ParamType1,
    arity: Optional[int] = None,
    **__kwargs,
) -> Callable[[ParamType2], Callable[[ParamType3], ReturnType]]: ...
@overload
def curry(
    func: Callable[[ParamType1, ParamType2, ParamType3, ParamType4], ReturnType],
    arg: ParamType1,
    arity: Optional[int] = None,
    **__kwargs,
) -> Callable[
    [ParamType2], Callable[[ParamType3], Callable[[ParamType4], ReturnType]]
]: ...
@overload
def curry(
    func: Callable[
        [ParamType1, ParamType2, ParamType3, ParamType4, ParamType5], ReturnType
    ],
    arg: ParamType1,
    arity: Optional[int] = None,
    **__kwargs,
) -> Callable[
    [ParamType2],
    Callable[[ParamType3], Callable[[ParamType4], Callable[[ParamType5], ReturnType]]],
]: ...
