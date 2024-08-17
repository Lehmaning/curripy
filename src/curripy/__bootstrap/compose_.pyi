from typing import Callable, overload

from ..__generics import (
    ArgKwargP,
    ParamT,
    ReturnT,
    ReturnT1,
    ReturnT2,
    ReturnT3,
    ReturnT4,
    ReturnT5,
)
from ..utils import curry

__all__ = (
    "cdot",
    "dot",
    "compose",
    "pipe",
)

def dot(
    f: Callable[[ParamT], ReturnT1], g: Callable[[ReturnT1], ReturnT2]
) -> Callable[[ParamT], ReturnT2]: ...
cdot = curry(dot, arity=2)
@overload
def pipe(
    func1: Callable[ArgKwargP, ReturnT1],
) -> Callable[ArgKwargP, ReturnT1]: ...
@overload
def pipe(
    func1: Callable[[ParamT], ReturnT1],
    func2: Callable[[ReturnT1], ReturnT2],
) -> Callable[[ParamT], ReturnT2]: ...
@overload
def pipe(
    func1: Callable[[ParamT], ReturnT1],
    func2: Callable[[ReturnT1], ReturnT2],
    func3: Callable[[ReturnT2], ReturnT3],
) -> Callable[[ParamT], ReturnT3]: ...
@overload
def pipe(
    func1: Callable[[ParamT], ReturnT1],
    func2: Callable[[ReturnT1], ReturnT2],
    func3: Callable[[ReturnT2], ReturnT3],
    func4: Callable[[ReturnT3], ReturnT4],
) -> Callable[[ParamT], ReturnT4]: ...
@overload
def pipe(
    func1: Callable[[ParamT], ReturnT1],
    func2: Callable[[ReturnT1], ReturnT2],
    func3: Callable[[ReturnT2], ReturnT3],
    func4: Callable[[ReturnT3], ReturnT4],
    func5: Callable[[ReturnT4], ReturnT5],
) -> Callable[[ParamT], ReturnT5]: ...
@overload
def compose(
    func1: Callable[ArgKwargP, ReturnT],
) -> Callable[ArgKwargP, ReturnT]: ...
@overload
def compose(
    func2: Callable[[ReturnT1], ReturnT2],
    func1: Callable[[ParamT], ReturnT1],
) -> Callable[[ParamT], ReturnT1]: ...
@overload
def compose(
    func3: Callable[[ReturnT2], ReturnT3],
    func2: Callable[[ReturnT1], ReturnT2],
    func1: Callable[[ParamT], ReturnT1],
) -> Callable[[ParamT], ReturnT3]: ...
@overload
def compose(
    func4: Callable[[ReturnT3], ReturnT4],
    func3: Callable[[ReturnT2], ReturnT3],
    func2: Callable[[ReturnT1], ReturnT2],
    func1: Callable[[ParamT], ReturnT1],
) -> Callable[[ParamT], ReturnT4]: ...
@overload
def compose(
    func5: Callable[[ReturnT4], ReturnT5],
    func4: Callable[[ReturnT3], ReturnT4],
    func3: Callable[[ReturnT2], ReturnT3],
    func2: Callable[[ReturnT1], ReturnT2],
    func1: Callable[[ParamT], ReturnT1],
) -> Callable[[ParamT], ReturnT5]: ...
