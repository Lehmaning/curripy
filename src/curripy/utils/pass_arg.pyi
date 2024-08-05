from typing import Concatenate, Callable

from ..__generics import ParamType, ReturnType, P

def pass_arg(
    arg: ParamType,
) -> Callable[[Callable[[ParamType], ReturnType]], ReturnType]: ...
def pass_arg_(
    arg: ParamType, obj: Callable[[ParamType], ReturnType]
) -> ReturnType: ...