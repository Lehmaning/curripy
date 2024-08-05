from typing import Concatenate, Callable, Iterable
from ..__generics import ParamType, ReturnType, P

def filter_(
    func: Callable[[ParamType], ReturnType] | None,
) -> Callable[[Iterable[ParamType]], filter[ReturnType]]: ...
def map_(
    func: Callable[[ParamType], ReturnType] | None,
) -> Callable[Concatenate[Iterable[ParamType], P], filter[ReturnType]]: ...
