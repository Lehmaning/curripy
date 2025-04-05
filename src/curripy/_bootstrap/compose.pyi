from typing import Callable, overload

from curripy.__generics import (
    ArgKwargP,
    ReturnT,
    ReturnT1,
    ReturnT2,
    ReturnT3,
    ReturnT4,
    ReturnT5,
)
from curripy.utils import curry

__all__ = (
    "dot",
    "cdot",
    "compose",
    "pipe",
)

def dot(
    f: Callable[ArgKwargP, ReturnT1], g: Callable[[ReturnT1], ReturnT2]
) -> Callable[ArgKwargP, ReturnT2]:
    """
    A function that acts lke '.' in Haskell, which does not mean the dot operator between matrices.

    Args:
        f (Callable[ArgKwargP, ReturnT1]): first function
        g (Callable[[ReturnT1], ReturnT2]): second function

    Returns:
        Callable[ArgKwargP, ReturnT2]: composed function
    """
    ...

cdot = curry(dot, arity=2)
"""Same as dot, but curried."""

@overload
def pipe(
    func1: Callable[ArgKwargP, ReturnT1],
) -> Callable[ArgKwargP, ReturnT1]: ...
@overload
def pipe(
    func1: Callable[ArgKwargP, ReturnT1],
    func2: Callable[[ReturnT1], ReturnT2],
) -> Callable[ArgKwargP, ReturnT2]: ...
@overload
def pipe(
    func1: Callable[ArgKwargP, ReturnT1],
    func2: Callable[[ReturnT1], ReturnT2],
    func3: Callable[[ReturnT2], ReturnT3],
) -> Callable[ArgKwargP, ReturnT3]: ...
@overload
def pipe(
    func1: Callable[ArgKwargP, ReturnT1],
    func2: Callable[[ReturnT1], ReturnT2],
    func3: Callable[[ReturnT2], ReturnT3],
    func4: Callable[[ReturnT3], ReturnT4],
) -> Callable[ArgKwargP, ReturnT4]: ...
@overload
def pipe(
    func1: Callable[ArgKwargP, ReturnT1],
    func2: Callable[[ReturnT1], ReturnT2],
    func3: Callable[[ReturnT2], ReturnT3],
    func4: Callable[[ReturnT3], ReturnT4],
    func5: Callable[[ReturnT4], ReturnT5],
) -> Callable[ArgKwargP, ReturnT5]: ...
@overload
def compose(
    func1: Callable[ArgKwargP, ReturnT],
) -> Callable[ArgKwargP, ReturnT]: ...
@overload
def compose(
    func2: Callable[[ReturnT1], ReturnT2],
    func1: Callable[ArgKwargP, ReturnT1],
) -> Callable[ArgKwargP, ReturnT1]: ...
@overload
def compose(
    func3: Callable[[ReturnT2], ReturnT3],
    func2: Callable[[ReturnT1], ReturnT2],
    func1: Callable[ArgKwargP, ReturnT1],
) -> Callable[ArgKwargP, ReturnT3]: ...
@overload
def compose(
    func4: Callable[[ReturnT3], ReturnT4],
    func3: Callable[[ReturnT2], ReturnT3],
    func2: Callable[[ReturnT1], ReturnT2],
    func1: Callable[ArgKwargP, ReturnT1],
) -> Callable[ArgKwargP, ReturnT4]: ...
@overload
def compose(
    func5: Callable[[ReturnT4], ReturnT5],
    func4: Callable[[ReturnT3], ReturnT4],
    func3: Callable[[ReturnT2], ReturnT3],
    func2: Callable[[ReturnT1], ReturnT2],
    func1: Callable[ArgKwargP, ReturnT1],
) -> Callable[ArgKwargP, ReturnT5]: ...
