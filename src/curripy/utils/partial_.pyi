from typing import (
    Iterable,
    TypeGuard,
    Sequence,
    Any,
    Callable,
    ParamSpec,
    TypeVar,
    overload,
)
from ..__generics import (
    P,
    ReturnType,
    ParamType1,
    ParamType2,
    ParamType3,
    ParamType4,
    ParamType5,
)

@overload
def partial(func: Callable[P, ReturnType]) -> Callable[P, ReturnType]: ...
@overload
def partial(
    func: Callable[[ParamType1], ReturnType], arg1: ParamType1, **kwargs: Any
) -> Callable[[ParamType1], ReturnType]: ...
@overload
def partial(
    func: type[filter[Any]],
    arg1: Callable[[ParamType1], bool | TypeGuard[ParamType1]] | None,
    **kwargs,
) -> Callable[[Iterable[ParamType1 | None]], filter[ParamType1]]: ...
@overload
def partial(
    func: Callable[[ParamType1, ParamType2], ReturnType], arg1: ParamType1, **kwargs
) -> Callable[[ParamType2], ReturnType]: ...
@overload
def partial(
    func: Callable[[ParamType1, ParamType2, ParamType3], ReturnType],
    arg1: ParamType1,
    arg2: ParamType2,
    **kwargs: Any,
) -> Callable[[ParamType3], ReturnType]: ...
@overload
def partial(
    func: Callable[[ParamType1, ParamType2, ParamType3, ParamType4], ReturnType],
    arg1: ParamType1,
    arg2: ParamType2,
    arg3: ParamType3,
    **kwargs: Any,
) -> Callable[[ParamType4], ReturnType]: ...
@overload
def partial(
    func: Callable[
        [ParamType1, ParamType2, ParamType3, ParamType4, ParamType5], ReturnType
    ],
    arg1: ParamType1,
    arg2: ParamType2,
    arg3: ParamType3,
    arg4: ParamType4,
    **kwargs: Any,
) -> Callable[[ParamType5], ReturnType]: ...
