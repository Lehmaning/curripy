from .curry_ import curry
from typing import Concatenate, Callable
from ..__generics import ParamType, ReturnType, P

def pass_arg_(
    arg,
    func: Callable[Concatenate[ParamType, P], ReturnType],
    *args: P.args,
    **kwargs: P.kwargs,
) -> ReturnType: ...
def pass_arg(
    arg: ParamType,
) -> Callable[[Callable[[ParamType], ReturnType]], ReturnType]: ...
