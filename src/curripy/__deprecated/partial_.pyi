from typing import (
    Callable,
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

# 1th stage type gymnastics
@overload
def partial(func: Callable[P, ReturnType]) -> Callable[P, ReturnType]: ...
# 2th stage type gymnastics
# @overload
# def partial(
#     func: type[filter[Any]],
#     arg1: Callable[[ParamType2], TypeGuard[ParamType1] | bool] | None,
#
# ) -> Callable[[Iterable[ParamType2 | None]], filter[ParamType1]]:
#     """Hard-coded type gymnastics for filter. Without this mypy would throw an arg-type error"""
#     ...
@overload
def partial(
    func: Callable[[ParamType1, ParamType2], ReturnType], arg2: ParamType2
) -> Callable[[ParamType1], ReturnType]: ...
@overload
def partial(
    func: Callable[[ParamType1, ParamType2], ReturnType], arg1: ParamType1
) -> Callable[[ParamType2], ReturnType]: ...

# 3th stage type gymnastics
@overload
def partial(
    func: Callable[[ParamType1, ParamType2, ParamType3], ReturnType],
    arg1: ParamType1,
    arg2: ParamType2,
) -> Callable[[ParamType3], ReturnType]: ...
@overload
def partial(
    func: Callable[[ParamType1, ParamType2, ParamType3], ReturnType],
    arg1: ParamType1,
    arg3: ParamType3,
) -> Callable[[ParamType2], ReturnType]: ...
@overload
def partial(
    func: Callable[[ParamType1, ParamType2, ParamType3], ReturnType],
    arg2: ParamType2,
    arg3: ParamType3,
) -> Callable[[ParamType1], ReturnType]: ...

# 4th stage type gymnastics
@overload
def partial(
    func: Callable[[ParamType1, ParamType2, ParamType3, ParamType4], ReturnType],
    arg1: ParamType1,
) -> Callable[[ParamType2, ParamType3, ParamType4], ReturnType]: ...
@overload
def partial(
    func: Callable[[ParamType1, ParamType2, ParamType3, ParamType4], ReturnType],
    arg2: ParamType2,
) -> Callable[[ParamType1, ParamType3, ParamType4], ReturnType]: ...
@overload
def partial(
    func: Callable[[ParamType1, ParamType2, ParamType3, ParamType4], ReturnType],
    arg3: ParamType3,
) -> Callable[[ParamType1, ParamType2, ParamType4], ReturnType]: ...
@overload
def partial(
    func: Callable[[ParamType1, ParamType2, ParamType3, ParamType4], ReturnType],
    arg4: ParamType4,
) -> Callable[[ParamType1, ParamType2, ParamType3], ReturnType]: ...
@overload
def partial(
    func: Callable[[ParamType1, ParamType2, ParamType3, ParamType4], ReturnType],
    arg1: ParamType1,
    arg2: ParamType2,
) -> Callable[[ParamType3, ParamType4], ReturnType]: ...
@overload
def partial(
    func: Callable[[ParamType1, ParamType2, ParamType3, ParamType4], ReturnType],
    arg1: ParamType1,
    arg3: ParamType3,
) -> Callable[[ParamType2, ParamType4], ReturnType]: ...
@overload
def partial(
    func: Callable[[ParamType1, ParamType2, ParamType3, ParamType4], ReturnType],
    arg1: ParamType1,
    arg4: ParamType4,
) -> Callable[[ParamType2, ParamType3], ReturnType]: ...
@overload
def partial(
    func: Callable[[ParamType1, ParamType2, ParamType3, ParamType4], ReturnType],
    arg2: ParamType2,
    arg3: ParamType3,
) -> Callable[[ParamType1, ParamType4], ReturnType]: ...
@overload
def partial(
    func: Callable[[ParamType1, ParamType2, ParamType3, ParamType4], ReturnType],
    arg2: ParamType2,
    arg4: ParamType4,
) -> Callable[[ParamType1, ParamType3], ReturnType]: ...
@overload
def partial(
    func: Callable[[ParamType1, ParamType2, ParamType3, ParamType4], ReturnType],
    arg3: ParamType3,
    arg4: ParamType4,
) -> Callable[[ParamType1, ParamType2], ReturnType]: ...
@overload
def partial(
    func: Callable[[ParamType1, ParamType2, ParamType3, ParamType4], ReturnType],
    arg1: ParamType1,
    arg2: ParamType2,
    arg3: ParamType3,
) -> Callable[[ParamType4], ReturnType]: ...
@overload
def partial(
    func: Callable[[ParamType1, ParamType2, ParamType3, ParamType4], ReturnType],
    arg1: ParamType1,
    arg2: ParamType2,
    arg4: ParamType4,
) -> Callable[[ParamType3], ReturnType]: ...
@overload
def partial(
    func: Callable[[ParamType1, ParamType2, ParamType3, ParamType4], ReturnType],
    arg1: ParamType1,
    arg3: ParamType3,
    arg4: ParamType4,
) -> Callable[[ParamType2], ReturnType]: ...
@overload
def partial(
    func: Callable[[ParamType1, ParamType2, ParamType3, ParamType4], ReturnType],
    arg2: ParamType2,
    arg3: ParamType3,
    arg4: ParamType4,
) -> Callable[[ParamType1], ReturnType]: ...

# 5th
@overload
def partial(
    func: Callable[
        [ParamType1, ParamType2, ParamType3, ParamType4, ParamType5], ReturnType
    ],
    arg1: ParamType1,
    arg2: ParamType2,
    arg3: ParamType3,
    arg4: ParamType4,
) -> Callable[[ParamType5], ReturnType]: ...

@overload
def partial(
    func: Callable[P, ReturnType], *args: P.args, **kwargs: P.kwargs
) -> Callable[[], ReturnType]: ...
