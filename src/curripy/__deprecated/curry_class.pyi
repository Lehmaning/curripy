from typing import (
    Callable,
    Concatenate,
    Generic,
    Literal,
    ParamSpec,
    TypeVar,
    overload,
)

from ..__generics import (
    ParamT1,
    ParamT2,
    ParamT3,
    ParamT4,
    ParamT5,
    ReturnT,
    ArgKwargP 
)

class Curry(Generic[ParamT1, ReturnT, ArgKwargP]):
    def __init__(
        self,
        func: Callable[ArgKwargP, ReturnT],
        arity: None = None,
    ) -> None: ...
    def __call__(self, *args, **kwargs): ...
    def __repr__(self): ...
    def set_args(self, *args, **kwargs): ...
    def set_kwargs(self, *args, **kwargs): ...

class Curry1(Curry[ParamT1, ReturnT, ArgKwargP]):
    def __call__(self, arg1: ParamT1, **kwargs) -> ReturnT: ...

class Curry2(Curry[ParamT1, Curry1[ParamT2, ReturnT, ArgKwargP], ArgKwargP]):
    def __call__(self, *args, **kwargs): ...

class Curry3(Curry[ParamT1, Curry2[ParamT2, ParamT3, ReturnT, ArgKwargP], ArgKwargP]):
    @overload
    def __call__(
        self, arg1: ParamT1, **kwargs
    ) -> Curry2[ParamT2, ParamT3, ReturnT, ArgKwargP]: ...
    @overload
    def __call__(
        self, arg1: ParamT1, arg2: ParamT2, **kwargs
    ) -> Curry1[ParamT3, ReturnT, ArgKwargP]: ...
    @overload
    def __call__(
        self, arg1: ParamT1, arg2: ParamT2, arg3: ParamT3, **kwargs
    ) -> ReturnT: ...
    def __call__(self, *args, **kwargs): ...

class Curry4(
    Curry[ParamT1, Curry3[ParamT2, ParamT3, ParamT4, ReturnT, ArgKwargP], ArgKwargP]
):
    @overload
    def __call__(
        self, arg1: ParamT1, **kwargs
    ) -> Curry3[ParamT2, ParamT3, ParamT4, ReturnT, ArgKwargP]: ...
    @overload
    def __call__(
        self, arg1: ParamT1, arg2: ParamT2, **kwargs
    ) -> Curry2[ParamT3, ParamT4, ReturnT, ArgKwargP]: ...
    @overload
    def __call__(
        self, arg1: ParamT1, arg2: ParamT2, arg3: ParamT3, **kwargs
    ) -> Curry1[ParamT4, ReturnT, ArgKwargP]: ...
    @overload
    def __call__(
        self,
        arg1: ParamT1,
        arg2: ParamT2,
        arg3: ParamT3,
        arg4: ParamT4,
    ) -> ReturnT: ...
    def __call__(self, *args, **kwargs): ...

class Curry5(
    Curry[
        ParamT1,
        Curry4[ParamT2, ParamT3, ParamT4, ParamT5, ReturnT, ArgKwargP],
        ArgKwargP 
    ]
):
    @overload
    def __call__(
        self, arg1: ParamT1, **kwargs
    ) -> Curry4[ParamT2, ParamT3, ParamT4, ParamT5, ReturnT, ArgKwargP]: ...
    @overload
    def __call__(
        self, arg1: ParamT1, arg2: ParamT2, **kwargs
    ) -> Curry3[ParamT3, ParamT4, ParamT5, ReturnT, ArgKwargP]: ...
    @overload
    def __call__(
        self, arg1: ParamT1, arg2: ParamT2, arg3: ParamT3, **kwargs
    ) -> Curry2[ParamT4, ParamT5, ReturnT, ArgKwargP]: ...
    @overload
    def __call__(
        self,
        arg1: ParamT1,
        arg2: ParamT2,
        arg3: ParamT3,
        arg4: ParamT4,
        **kwargs,
    ) -> Curry1[ParamT5, ReturnT, ArgKwargP]: 
        return super().__call__(arg1, arg2, arg3, arg4)
    @overload
    def __call__(
        self,
        arg1: ParamT1,
        arg2: ParamT2,
        arg3: ParamT3,
        arg4: ParamT4,
        arg5: ParamT5,
        **kwargs,
    ) -> ReturnT: ...

@overload
def curry(
    func: Callable[[ParamT1], ReturnT], arity: None = None
) -> Curry1[ParamT1, ReturnT, ArgKwargP]: ...
@overload
def curry(
    func: Callable[[ParamT1, ParamT2], ReturnT], arity: None = None
) -> Curry2[ParamT1, ParamT2, ReturnT, ArgKwargP]: ...
@overload
def curry(
    func: Callable[[ParamT1, ParamT2, ParamT3], ReturnT],
    arity: None = None,
) -> Curry3[ParamT1, ParamT2, ParamT3, ReturnT, ArgKwargP]: ...
@overload
def curry(
    func: Callable[[ParamT1, ParamT2, ParamT3, ParamT4], ReturnT],
    arity: None = None,
) -> Curry4[ParamT1, ParamT2, ParamT3, ParamT4, ReturnT, ArgKwargP]: ...
@overload
def curry(
    func: Callable[
        [ParamT1, ParamT2, ParamT3, ParamT4, ParamT5], ReturnT
    ],
    arity: None = None,
) -> Curry5[
    ParamT1, ParamT2, ParamT3, ParamT4, ParamT5, ReturnT, P
]: ...
@overload
def curry(
    func: Callable[Concatenate[ParamT1, ArgKwargP], ReturnT],
    arity: Literal[1],
) -> Curry1[ParamT1, ReturnT, ArgKwargP]: ...
@overload
def curry(
    func: Callable[Concatenate[ParamT1, ParamT2, ArgKwargP], ReturnT],
    arity: Literal[2],
) -> Curry2[ParamT1, ParamT2, ReturnT, ArgKwargP]: ...
@overload
def curry(
    func: Callable[Concatenate[ParamT1, ParamT2, ParamT3, ArgKwargP], ReturnT],
    arity: Literal[3],
) -> Curry3[ParamT1, ParamT2, ParamT3, ReturnT, ArgKwargP]: ...
@overload
def curry(
    func: Callable[
        Concatenate[ParamT1, ParamT2, ParamT3, ParamT4, ArgKwargP], ReturnT
    ],
    arity: Literal[4],
) -> Curry4[ParamT1, ParamT2, ParamT3, ParamT4, ReturnT, ArgKwargP]: ...
@overload
def curry(
    func: Callable[
        Concatenate[ParamT1, ParamT2, ParamT3, ParamT4, ParamT5, ArgKwargP],
        ReturnT,
    ],
    arity: Literal[5],
) -> Curry5[
    ParamT1, ParamT2, ParamT3, ParamT4, ParamT5, ReturnT, P
]: ...
def curry(func: Callable[ArgKwargP, ReturnT], arity: None | int = None): ...
@overload
def curry_right(
    func: Callable[
        [ParamT1, ParamT2, ParamT3, ParamT4, ParamT5], ReturnT
    ],
    arity: None = None,
) -> Curry5[
    ParamT5, ParamT4, ParamT3, ParamT2, ParamT1, ReturnT, P
]: ...
@overload
def curry_right(
    func: Callable[[ParamT1, ParamT2, ParamT3, ParamT4], ReturnT],
    arity: None = None,
) -> Curry4[ParamT4, ParamT3, ParamT2, ParamT1, ReturnT, ArgKwargP]: ...
@overload
def curry_right(
    func: Callable[[ParamT1, ParamT2, ParamT3], ReturnT],
    arity: None = None,
) -> Curry3[ParamT3, ParamT2, ParamT1, ReturnT, ArgKwargP]: ...
@overload
def curry_right(
    func: Callable[[ParamT1, ParamT2], ReturnT],
    arity: None = None,
) -> Curry2[ParamT2, ParamT1, ReturnT, ArgKwargP]: ...
@overload
def curry_right(
    func: Callable[[ParamT1], ReturnT],
    arity: None = None,
) -> Curry1[ParamT1, ReturnT, ArgKwargP]: ...
@overload
def curry_right(
    func: Callable[
        Concatenate[ParamT1, ParamT2, ParamT3, ParamT4, ParamT5, ArgKwargP],
        ReturnT,
    ],
    arity: Literal[5],
) -> Curry5[
    ParamT5, ParamT4, ParamT3, ParamT2, ParamT1, ReturnT, P
]: ...
@overload
def curry_right(
    func: Callable[
        Concatenate[ParamT1, ParamT2, ParamT3, ParamT4, ArgKwargP], ReturnT
    ],
    arity: Literal[4],
) -> Curry4[ParamT4, ParamT3, ParamT2, ParamT1, ReturnT, ArgKwargP]: ...
@overload
def curry_right(
    func: Callable[Concatenate[ParamT1, ParamT2, ParamT3, ArgKwargP], ReturnT],
    arity: Literal[3],
) -> Curry3[ParamT3, ParamT2, ParamT1, ReturnT, ArgKwargP]: ...
@overload
def curry_right(
    func: Callable[Concatenate[ParamT1, ParamT2, ArgKwargP], ReturnT],
    arity: Literal[2],
) -> Curry2[ParamT2, ParamT1, ReturnT, ArgKwargP]: ...
@overload
def curry_right(
    func: Callable[Concatenate[ParamT1, ArgKwargP], ReturnT],
    arity: Literal[1],
) -> Curry1[ParamT1, ReturnT, ArgKwargP]: ...
def curry_right(func: Callable[ArgKwargP, ReturnT], arity: None | int = None): ...
