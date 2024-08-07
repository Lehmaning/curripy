from typing import overload, Generator, Callable, Iterable
from functools import reduce
from ..__generics import ParamType1, ParamType2
from ..__dummies.obj import obejct_ as __initial_missing

def reduce_generator(
    func: Callable[[ParamType1, ParamType2], ParamType1],
    sequence: Iterable[ParamType2],
    initial: ParamType1 | object = __initial_missing,
) -> Generator[ParamType1, None, None]: ...
