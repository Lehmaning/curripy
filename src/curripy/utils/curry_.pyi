from typing import (
    Callable,
    Concatenate,
    Literal,
    overload,
)

from ..__generics import ArgKwargP, ParamT1, ParamT2, ParamT3, ParamT4, ParamT5, ReturnT

__all__ = (
    "curry",
    "curry_right",
)
Func1 = Callable[[ParamT1], ReturnT]
Func2 = Callable[[ParamT1, ParamT2], ReturnT]
Func3 = Callable[[ParamT1, ParamT2, ParamT3], ReturnT]
Func4 = Callable[[ParamT1, ParamT2, ParamT3, ParamT4], ReturnT]
Func5 = Callable[[ParamT1, ParamT2, ParamT3, ParamT4, ParamT5], ReturnT]
Curried1 = Callable[[ParamT1], ReturnT]
Curried2 = Callable[[ParamT1], Callable[[ParamT2], ReturnT]]
Curried3 = Callable[[ParamT1], Callable[[ParamT2], Callable[[ParamT3], ReturnT]]]
Curried4 = Callable[
    [ParamT1], Callable[[ParamT2], Callable[[ParamT3], Callable[[ParamT4], ReturnT]]]
]
Curried5 = Callable[
    [ParamT1],
    Callable[
        [ParamT2],
        Callable[[ParamT3], Callable[[ParamT4], Callable[[ParamT5], ReturnT]]],
    ],
]
CurriedRight1 = Callable[[ParamT1], ReturnT]
CurriedRight2 = Callable[[ParamT2], Callable[[ParamT1], ReturnT]]
CurriedRight3 = Callable[[ParamT3], Callable[[ParamT2], Callable[[ParamT1], ReturnT]]]
CurriedRight4 = Callable[
    [ParamT4], Callable[[ParamT3], Callable[[ParamT2], Callable[[ParamT1], ReturnT]]]
]
CurriedRight5 = Callable[
    [ParamT5],
    Callable[
        [ParamT4],
        Callable[[ParamT3], Callable[[ParamT2], Callable[[ParamT1], ReturnT]]],
    ],
]
CurriedSplitArgKwargs1 = Callable[[ParamT1], Callable[ArgKwargP, ReturnT]]
CurriedArgKwargs2 = Callable[
    [ParamT1], Callable[Concatenate[ParamT2, ArgKwargP], ReturnT]
]
CurriedArgKwargs3 = Callable[
    [ParamT1], Callable[[ParamT2], Callable[Concatenate[ParamT3, ArgKwargP], ReturnT]]
]
CurriedArgKwargs4 = Callable[
    [ParamT1],
    Callable[
        [ParamT2],
        Callable[[ParamT3], Callable[Concatenate[ParamT4, ArgKwargP], ReturnT]],
    ],
]
CurriedArgKwargs5 = Callable[
    [ParamT1],
    Callable[
        [ParamT2],
        Callable[
            [ParamT3],
            Callable[[ParamT4], Callable[Concatenate[ParamT5, ArgKwargP], ReturnT]],
        ],
    ],
]
CurriedRightArgKwargs2 = Callable[
    [ParamT2], Callable[Concatenate[ParamT1, ArgKwargP], ReturnT]
]
CurriedRightArgKwargs3 = Callable[
    [ParamT3],
    Callable[[ParamT2], Callable[Concatenate[ParamT1, ArgKwargP], ReturnT]],
]
CurriedRightArgKwargs4 = Callable[
    [ParamT4],
    Callable[
        [ParamT3],
        Callable[[ParamT2], Callable[Concatenate[ParamT1, ArgKwargP], ReturnT]],
    ],
]
CurriedRightArgKwargs5 = Callable[
    [ParamT5],
    Callable[
        [ParamT4],
        Callable[
            [ParamT3],
            Callable[
                [ParamT2], Callable[Concatenate[ParamT1, ArgKwargP], ReturnT]
            ],
        ],
    ],
]
FuncArgKwargs1 = Callable[Concatenate[ParamT1, ArgKwargP], ReturnT]
FuncArgKwargs2 = Callable[Concatenate[ParamT1, ParamT2, ArgKwargP], ReturnT]
FuncArgKwargs3 = Callable[Concatenate[ParamT1, ParamT2, ParamT3, ArgKwargP], ReturnT]
FuncArgKwargs4 = Callable[
    Concatenate[ParamT1, ParamT2, ParamT3, ParamT4, ArgKwargP], ReturnT
]
FuncArgKwargs5 = Callable[
    Concatenate[ParamT1, ParamT2, ParamT3, ParamT4, ParamT5, ArgKwargP], ReturnT
]
FuncKwargs = Callable[ArgKwargP, ReturnT]

@overload
def curry(
    func: Func1[ParamT1, ReturnT], arity: None = ...
) -> Curried1[ParamT1, ReturnT]: ...
@overload
def curry(
    func: Func2[ParamT1, ParamT2, ReturnT], arity: None = ...
) -> Curried2[ParamT1, ParamT2, ReturnT]: ...
@overload
def curry(
    func: Func3[ParamT1, ParamT2, ParamT3, ReturnT], arity: None = ...
) -> Curried3[ParamT1, ParamT2, ParamT3, ReturnT]: ...
@overload
def curry(
    func: Func4[ParamT1, ParamT2, ParamT3, ParamT4, ReturnT], arity: None = ...
) -> Curried4[ParamT1, ParamT2, ParamT3, ParamT4, ReturnT]: ...
@overload
def curry(
    func: Func5[ParamT1, ParamT2, ParamT3, ParamT4, ParamT5, ReturnT], arity: None = ...
) -> Curried5[ParamT1, ParamT2, ParamT3, ParamT4, ParamT5, ReturnT]: ...
@overload
def curry(
    func: FuncArgKwargs5[
        ParamT1, ParamT2, ParamT3, ParamT4, ParamT5, ArgKwargP, ReturnT
    ],
    arity: Literal[5],
) -> CurriedArgKwargs5[
    ParamT1, ParamT2, ParamT3, ParamT4, ParamT5, ArgKwargP, ReturnT
]: ...
@overload
def curry(
    func: FuncArgKwargs4[ParamT1, ParamT2, ParamT3, ParamT4, ArgKwargP, ReturnT],
    arity: Literal[4],
) -> CurriedArgKwargs4[ParamT1, ParamT2, ParamT3, ParamT4, ArgKwargP, ReturnT]: ...
@overload
def curry(
    func: FuncArgKwargs3[ParamT1, ParamT2, ParamT3, ArgKwargP, ReturnT],
    arity: Literal[3],
) -> CurriedArgKwargs3[ParamT1, ParamT2, ParamT3, ArgKwargP, ReturnT]: ...
@overload
def curry(
    func: FuncArgKwargs1[ParamT1, ArgKwargP, ReturnT],
    arity: Literal[2],
) -> CurriedSplitArgKwargs1[ParamT1, ArgKwargP, ReturnT]: ...
@overload
def curry(
    func: FuncArgKwargs2[ParamT1, ParamT2, ArgKwargP, ReturnT],
    arity: Literal[2],
) -> CurriedArgKwargs2[ParamT1, ParamT2, ArgKwargP, ReturnT]: ...
@overload
def curry(
    func: Callable[ArgKwargP, ReturnT],
    arity: Literal[1],
) -> Callable[ArgKwargP, ReturnT]: ...
@overload
def curry(
    func: None, arity: Literal[1]
) -> Callable[
    [FuncArgKwargs1[ParamT1, ArgKwargP, ReturnT]],
    CurriedSplitArgKwargs1[ParamT1, ArgKwargP, ReturnT],
]: ...
@overload
def curry(
    func: None, arity: Literal[2]
) -> Callable[
    [FuncArgKwargs2[ParamT1, ParamT2, ArgKwargP, ReturnT]],
    CurriedArgKwargs2[ParamT1, ParamT2, ArgKwargP, ReturnT],
]: ...
@overload
def curry(
    func: None, arity: Literal[3]
) -> Callable[
    [FuncArgKwargs3[ParamT1, ParamT2, ParamT3, ArgKwargP, ReturnT]],
    CurriedArgKwargs3[ParamT1, ParamT2, ParamT3, ArgKwargP, ReturnT],
]: ...
@overload
def curry(
    func: None, arity: Literal[4]
) -> Callable[
    [FuncArgKwargs4[ParamT1, ParamT2, ParamT3, ParamT4, ArgKwargP, ReturnT]],
    CurriedArgKwargs4[ParamT1, ParamT2, ParamT3, ParamT4, ArgKwargP, ReturnT],
]: ...
@overload
def curry(
    func: None, arity: Literal[5]
) -> Callable[
    [FuncArgKwargs5[ParamT1, ParamT2, ParamT3, ParamT4, ParamT5, ArgKwargP, ReturnT]],
    CurriedArgKwargs5[ParamT1, ParamT2, ParamT3, ParamT4, ParamT5, ArgKwargP, ReturnT],
]: ...
@overload
def curry_right(
    func: Func1[ParamT1, ReturnT], arity: None = ...
) -> CurriedRight1[ParamT1, ReturnT]: ...
@overload
def curry_right(
    func: Func2[ParamT1, ParamT2, ReturnT], arity: None = ...
) -> CurriedRight2[ParamT2, ParamT1, ReturnT]: ...
@overload
def curry_right(
    func: Func3[ParamT1, ParamT2, ParamT3, ReturnT], arity: None = ...
) -> CurriedRight3[ParamT3, ParamT2, ParamT1, ReturnT]: ...
@overload
def curry_right(
    func: Func4[ParamT1, ParamT2, ParamT3, ParamT4, ReturnT], arity: None = ...
) -> CurriedRight4[ParamT4, ParamT3, ParamT2, ParamT1, ReturnT]: ...
@overload
def curry_right(
    func: Func5[ParamT1, ParamT2, ParamT3, ParamT4, ParamT5, ReturnT], arity: None = ...
) -> CurriedRight5[ParamT5, ParamT4, ParamT3, ParamT2, ParamT1, ReturnT]: ...
@overload
def curry_right(
    func: FuncArgKwargs5[
        ParamT1, ParamT2, ParamT3, ParamT4, ParamT5, ArgKwargP, ReturnT
    ],
    arity: Literal[5],
) -> CurriedRightArgKwargs5[
    ParamT5, ParamT4, ParamT3, ParamT2, ParamT1, ArgKwargP, ReturnT
]: ...
@overload
def curry_right(
    func: FuncArgKwargs4[ParamT1, ParamT2, ParamT3, ParamT4, ArgKwargP, ReturnT],
    arity: Literal[4],
) -> CurriedRightArgKwargs4[ParamT4, ParamT3, ParamT2, ParamT1, ArgKwargP, ReturnT]: ...
@overload
def curry_right(
    func: FuncArgKwargs3[ParamT1, ParamT2, ParamT3, ArgKwargP, ReturnT],
    arity: Literal[3],
) -> CurriedRightArgKwargs3[ParamT3, ParamT2, ParamT1, ArgKwargP, ReturnT]: ...
@overload
def curry_right(
    func: FuncArgKwargs2[ParamT1, ParamT2, ArgKwargP, ReturnT], arity: Literal[2]
) -> CurriedRightArgKwargs2[ParamT2, ParamT1, ArgKwargP, ReturnT]: ...
@overload
def curry_right(
    func: FuncKwargs[ArgKwargP, ReturnT], arity: Literal[1]
) -> Callable[ArgKwargP, ReturnT]: ...
@overload
def curry_right(
    func: None, arity: Literal[1]
) -> Callable[
    [FuncArgKwargs1[ParamT1, ArgKwargP, ReturnT]],
    CurriedSplitArgKwargs1[ParamT1, ArgKwargP, ReturnT],
]: ...
@overload
def curry_right(
    func: None, arity: Literal[2]
) -> Callable[
    [FuncArgKwargs2[ParamT1, ParamT2, ArgKwargP, ReturnT]],
    CurriedRightArgKwargs2[ParamT2, ParamT1, ArgKwargP, ReturnT],
]: ...
@overload
def curry_right(
    func: None, arity: Literal[3]
) -> Callable[
    [FuncArgKwargs3[ParamT1, ParamT2, ParamT3, ArgKwargP, ReturnT]],
    CurriedRightArgKwargs3[ParamT3, ParamT2, ParamT1, ArgKwargP, ReturnT],
]: ...
@overload
def curry_right(
    func: None, arity: Literal[4]
) -> Callable[
    [FuncArgKwargs4[ParamT1, ParamT2, ParamT3, ParamT4, ArgKwargP, ReturnT]],
    CurriedRightArgKwargs4[ParamT4, ParamT3, ParamT2, ParamT1, ArgKwargP, ReturnT],
]: ...
@overload
def curry_right(
    func: None, arity: Literal[5]
) -> Callable[
    [FuncArgKwargs5[ParamT1, ParamT2, ParamT3, ParamT4, ParamT5, ArgKwargP, ReturnT]],
    CurriedRightArgKwargs5[
        ParamT5, ParamT4, ParamT3, ParamT2, ParamT1, ArgKwargP, ReturnT
    ],
]: ...
