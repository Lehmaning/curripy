from typing import Concatenate, ParamSpec, TypeVar, Callable

ParamType = TypeVar("ParamType")
ReturnType = TypeVar("ReturnType")
P = ParamSpec("P")

def pass_arg(
    arg,
    obj: Callable[Concatenate[ParamType, P], ReturnType],
    *args: P.args,
    **kwarg: P.kwargs,
) -> ReturnType: ...
