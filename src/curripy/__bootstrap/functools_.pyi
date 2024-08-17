from typing import Callable, Generator, Iterable

from ..__generics import ParamT1, ParamT2
from .dummies import obejct_ as __initial_missing
from ..__overlays.functools_ import lru_cache

__all__ = (
    "lru_cache",
    "reduce_generator",
)
def reduce_generator(
    func: Callable[[ParamT1, ParamT2], ParamT1],
    sequence: Iterable[ParamT2],
    initial: ParamT1 | object = __initial_missing,
) -> Generator[ParamT1, None, None]: ...
