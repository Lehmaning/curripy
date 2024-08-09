from typing import (
    Callable,
    Concatenate,
    overload,
)

from ..__generics import (
    ArgKwargP,
    ParamT1,
    ParamT2,
    ParamT3,
    ParamT4,
    ParamT5,
    ReturnT,
)

@overload
def partial(func: Callable[ArgKwargP, ReturnT]) -> Callable[ArgKwargP, ReturnT]: ...
@overload
def partial(
    func: Callable[Concatenate[ParamT1, ArgKwargP], ReturnT], arg1: ParamT1
) -> Callable[ArgKwargP, ReturnT]: ...
@overload
def partial(
    func: Callable[Concatenate[ParamT1, ParamT2, ArgKwargP], ReturnT],
    arg1: ParamT1,
    arg2: ParamT2,
) -> Callable[ArgKwargP, ReturnT]: ...
@overload
def partial(
    func: Callable[Concatenate[ParamT1, ParamT2, ParamT3, ArgKwargP], ReturnT],
    arg1: ParamT1,
    arg2: ParamT2,
    arg3: ParamT3,
) -> Callable[ArgKwargP, ReturnT]: ...
@overload
def partial(
    func: Callable[Concatenate[ParamT1, ParamT2, ParamT3, ParamT4, ArgKwargP], ReturnT],
    arg1: ParamT1,
    arg2: ParamT2,
    arg3: ParamT3,
    arg4: ParamT4,
) -> Callable[ArgKwargP, ReturnT]: ...
@overload
def partial(
    func: Callable[
        Concatenate[ParamT1, ParamT2, ParamT3, ParamT4, ParamT5, ArgKwargP],
        ReturnT,
    ],
    arg1: ParamT1,
    arg2: ParamT2,
    arg3: ParamT3,
    arg4: ParamT4,
    arg5: ParamT5,
) -> Callable[ArgKwargP, ReturnT]: ...
@overload
def partial(
    func: Callable[ArgKwargP, ReturnT],
    *args: ArgKwargP.args,
    **kwargs: ArgKwargP.kwargs,
) -> Callable[..., ReturnT]: ...
