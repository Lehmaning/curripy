from typing import (
    Callable,
    Concatenate,
    Literal,
    overload,
)

from ..__generics import (
    P,
    ParamType1,
    ParamType2,
    ParamType3,
    ParamType4,
    ParamType5,
    ReturnType,
)

@overload
def curry(
    func: Callable[[ParamType1], ReturnType],
    arity: None = None,
    **__kwargs,
) -> Callable[[ParamType1], ReturnType]: ...
@overload
def curry(
    func: Callable[[ParamType1, ParamType2], ReturnType],
    arity: None = None,
    **__kwargs,
) -> Callable[[ParamType1], Callable[[ParamType2], ReturnType]]: ...
@overload
def curry(
    func: Callable[[ParamType1, ParamType2, ParamType3], ReturnType],
    arity: None = None,
    **__kwargs,
) -> Callable[
    [ParamType1], Callable[[ParamType2], Callable[[ParamType3], ReturnType]]
]: ...
@overload
def curry(
    func: Callable[[ParamType1, ParamType2, ParamType3, ParamType4], ReturnType],
    arity: None = None,
    **__kwargs,
) -> Callable[
    [ParamType1],
    Callable[[ParamType2], Callable[[ParamType3], Callable[[ParamType4], ReturnType]]],
]: ...
@overload
def curry(
    func: Callable[
        [ParamType1, ParamType2, ParamType3, ParamType4, ParamType5], ReturnType
    ],
    arity: None = None,
    **__kwargs,
) -> Callable[
    [ParamType1],
    Callable[
        [ParamType2],
        Callable[
            [ParamType3], Callable[[ParamType4], Callable[[ParamType5], ReturnType]]
        ],
    ],
]: ...
@overload
def curry(
    func: Callable[Concatenate[ParamType1, P], ReturnType],
    arity: Literal[1],
    **__kwargs,
) -> Callable[Concatenate[ParamType1, P], ReturnType]: ...
@overload
def curry(
    func: Callable[Concatenate[ParamType1, ParamType2, P], ReturnType],
    arity: Literal[2],
    **__kwargs,
) -> Callable[[ParamType1], Callable[Concatenate[ParamType2, P], ReturnType]]: ...
@overload
def curry(
    func: Callable[Concatenate[ParamType1, ParamType2, ParamType3, P], ReturnType],
    arity: Literal[3],
    **__kwargs,
) -> Callable[
    [ParamType1],
    Callable[
        Concatenate[ParamType2, P], Callable[Concatenate[ParamType3, P], ReturnType]
    ],
]: ...
@overload
def curry(
    func: Callable[
        Concatenate[ParamType1, ParamType2, ParamType3, ParamType4, P], ReturnType
    ],
    arity: Literal[4],
    **__kwargs,
) -> Callable[
    [ParamType1],
    Callable[
        Concatenate[ParamType2, P],
        Callable[
            Concatenate[ParamType3, P], Callable[Concatenate[ParamType4, P], ReturnType]
        ],
    ],
]: ...
@overload
def curry(
    func: Callable[
        Concatenate[ParamType1, ParamType2, ParamType3, ParamType4, ParamType5, P],
        ReturnType,
    ],
    arity: Literal[5],
    **__kwargs,
) -> Callable[
    [ParamType1],
    Callable[
        Concatenate[ParamType2, P],
        Callable[
            Concatenate[ParamType3, P],
            Callable[
                Concatenate[ParamType4, P],
                Callable[Concatenate[ParamType5, P], ReturnType],
            ],
        ],
    ],
]: ...