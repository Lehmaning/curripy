from typing import Callable
from ..__generics import ParamType

def tap(
    func: Callable[[ParamType], None],
) -> Callable[[ParamType], ParamType]:
    ...
