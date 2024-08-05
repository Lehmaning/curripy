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
    ParamType1,
    ParamType2,
    ParamType3,
    ParamType4,
    ParamType5,
    ReturnType,
    P,
)

class Curry(Generic[ParamType1, ReturnType, P]):
    def __init__(
        self,
        func: Callable[P, ReturnType],
        arity: None = None,
    ) -> None: ...
    def __call__(self, *args, **kwargs): ...
    def __repr__(self): ...
    def set_args(self, *args, **kwargs): ...
    def set_kwargs(self, *args, **kwargs): ...

class Curry1(Curry[ParamType1, ReturnType, P]):
    def __call__(self, arg1: ParamType1, **kwargs) -> ReturnType: ...

class Curry2(Curry[ParamType1, Curry1[ParamType2, ReturnType, P], P]):
    def __call__(self, *args, **kwargs): ...

class Curry3(Curry[ParamType1, Curry2[ParamType2, ParamType3, ReturnType, P], P]):
    @overload
    def __call__(
        self, arg1: ParamType1, **kwargs
    ) -> Curry2[ParamType2, ParamType3, ReturnType, P]: ...
    @overload
    def __call__(
        self, arg1: ParamType1, arg2: ParamType2, **kwargs
    ) -> Curry1[ParamType3, ReturnType, P]: ...
    @overload
    def __call__(
        self, arg1: ParamType1, arg2: ParamType2, arg3: ParamType3, **kwargs
    ) -> ReturnType: ...
    def __call__(self, *args, **kwargs): ...

class Curry4(
    Curry[ParamType1, Curry3[ParamType2, ParamType3, ParamType4, ReturnType, P], P]
):
    @overload
    def __call__(
        self, arg1: ParamType1, **kwargs
    ) -> Curry3[ParamType2, ParamType3, ParamType4, ReturnType, P]: ...
    @overload
    def __call__(
        self, arg1: ParamType1, arg2: ParamType2, **kwargs
    ) -> Curry2[ParamType3, ParamType4, ReturnType, P]: ...
    @overload
    def __call__(
        self, arg1: ParamType1, arg2: ParamType2, arg3: ParamType3, **kwargs
    ) -> Curry1[ParamType4, ReturnType, P]: ...
    @overload
    def __call__(
        self,
        arg1: ParamType1,
        arg2: ParamType2,
        arg3: ParamType3,
        arg4: ParamType4,
    ) -> ReturnType: ...
    def __call__(self, *args, **kwargs): ...

class Curry5(
    Curry[
        ParamType1,
        Curry4[ParamType2, ParamType3, ParamType4, ParamType5, ReturnType, P],
        P,
    ]
):
    @overload
    def __call__(
        self, arg1: ParamType1, **kwargs
    ) -> Curry4[ParamType2, ParamType3, ParamType4, ParamType5, ReturnType, P]: ...
    @overload
    def __call__(
        self, arg1: ParamType1, arg2: ParamType2, **kwargs
    ) -> Curry3[ParamType3, ParamType4, ParamType5, ReturnType, P]: ...
    @overload
    def __call__(
        self, arg1: ParamType1, arg2: ParamType2, arg3: ParamType3, **kwargs
    ) -> Curry2[ParamType4, ParamType5, ReturnType, P]: ...
    @overload
    def __call__(
        self,
        arg1: ParamType1,
        arg2: ParamType2,
        arg3: ParamType3,
        arg4: ParamType4,
        **kwargs,
    ) -> Curry1[ParamType5, ReturnType, P]: 
        return super().__call__(arg1, arg2, arg3, arg4)
    @overload
    def __call__(
        self,
        arg1: ParamType1,
        arg2: ParamType2,
        arg3: ParamType3,
        arg4: ParamType4,
        arg5: ParamType5,
        **kwargs,
    ) -> ReturnType: ...

@overload
def curry(
    func: Callable[[ParamType1], ReturnType], arity: None = None
) -> Curry1[ParamType1, ReturnType, P]: ...
@overload
def curry(
    func: Callable[[ParamType1, ParamType2], ReturnType], arity: None = None
) -> Curry2[ParamType1, ParamType2, ReturnType, P]: ...
@overload
def curry(
    func: Callable[[ParamType1, ParamType2, ParamType3], ReturnType],
    arity: None = None,
) -> Curry3[ParamType1, ParamType2, ParamType3, ReturnType, P]: ...
@overload
def curry(
    func: Callable[[ParamType1, ParamType2, ParamType3, ParamType4], ReturnType],
    arity: None = None,
) -> Curry4[ParamType1, ParamType2, ParamType3, ParamType4, ReturnType, P]: ...
@overload
def curry(
    func: Callable[
        [ParamType1, ParamType2, ParamType3, ParamType4, ParamType5], ReturnType
    ],
    arity: None = None,
) -> Curry5[
    ParamType1, ParamType2, ParamType3, ParamType4, ParamType5, ReturnType, P
]: ...
@overload
def curry(
    func: Callable[Concatenate[ParamType1, P], ReturnType],
    arity: Literal[1],
) -> Curry1[ParamType1, ReturnType, P]: ...
@overload
def curry(
    func: Callable[Concatenate[ParamType1, ParamType2, P], ReturnType],
    arity: Literal[2],
) -> Curry2[ParamType1, ParamType2, ReturnType, P]: ...
@overload
def curry(
    func: Callable[Concatenate[ParamType1, ParamType2, ParamType3, P], ReturnType],
    arity: Literal[3],
) -> Curry3[ParamType1, ParamType2, ParamType3, ReturnType, P]: ...
@overload
def curry(
    func: Callable[
        Concatenate[ParamType1, ParamType2, ParamType3, ParamType4, P], ReturnType
    ],
    arity: Literal[4],
) -> Curry4[ParamType1, ParamType2, ParamType3, ParamType4, ReturnType, P]: ...
@overload
def curry(
    func: Callable[
        Concatenate[ParamType1, ParamType2, ParamType3, ParamType4, ParamType5, P],
        ReturnType,
    ],
    arity: Literal[5],
) -> Curry5[
    ParamType1, ParamType2, ParamType3, ParamType4, ParamType5, ReturnType, P
]: ...
def curry(func: Callable[P, ReturnType], arity: None | int = None): ...
@overload
def curry_right(
    func: Callable[
        [ParamType1, ParamType2, ParamType3, ParamType4, ParamType5], ReturnType
    ],
    arity: None = None,
) -> Curry5[
    ParamType5, ParamType4, ParamType3, ParamType2, ParamType1, ReturnType, P
]: ...
@overload
def curry_right(
    func: Callable[[ParamType1, ParamType2, ParamType3, ParamType4], ReturnType],
    arity: None = None,
) -> Curry4[ParamType4, ParamType3, ParamType2, ParamType1, ReturnType, P]: ...
@overload
def curry_right(
    func: Callable[[ParamType1, ParamType2, ParamType3], ReturnType],
    arity: None = None,
) -> Curry3[ParamType3, ParamType2, ParamType1, ReturnType, P]: ...
@overload
def curry_right(
    func: Callable[[ParamType1, ParamType2], ReturnType],
    arity: None = None,
) -> Curry2[ParamType2, ParamType1, ReturnType, P]: ...
@overload
def curry_right(
    func: Callable[[ParamType1], ReturnType],
    arity: None = None,
) -> Curry1[ParamType1, ReturnType, P]: ...
@overload
def curry_right(
    func: Callable[
        Concatenate[ParamType1, ParamType2, ParamType3, ParamType4, ParamType5, P],
        ReturnType,
    ],
    arity: Literal[5],
) -> Curry5[
    ParamType5, ParamType4, ParamType3, ParamType2, ParamType1, ReturnType, P
]: ...
@overload
def curry_right(
    func: Callable[
        Concatenate[ParamType1, ParamType2, ParamType3, ParamType4, P], ReturnType
    ],
    arity: Literal[4],
) -> Curry4[ParamType4, ParamType3, ParamType2, ParamType1, ReturnType, P]: ...
@overload
def curry_right(
    func: Callable[Concatenate[ParamType1, ParamType2, ParamType3, P], ReturnType],
    arity: Literal[3],
) -> Curry3[ParamType3, ParamType2, ParamType1, ReturnType, P]: ...
@overload
def curry_right(
    func: Callable[Concatenate[ParamType1, ParamType2, P], ReturnType],
    arity: Literal[2],
) -> Curry2[ParamType2, ParamType1, ReturnType, P]: ...
@overload
def curry_right(
    func: Callable[Concatenate[ParamType1, P], ReturnType],
    arity: Literal[1],
) -> Curry1[ParamType1, ReturnType, P]: ...
def curry_right(func: Callable[P, ReturnType], arity: None | int = None): ...
