from typing import Callable, Concatenate

from ..__generics import ArgKwargP, ParamT, ReturnT
from ..utils.curry_ import curry

def pass_arg_(
    arg: ParamT,
    func: Callable[Concatenate[ParamT, ArgKwargP], ReturnT],
    *args: ArgKwargP.args,
    **kwargs: ArgKwargP.kwargs,
) -> ReturnT: ...

def pass_arg(arg: ParamT) -> Callable[[Callable[[ParamT], ReturnT]], ReturnT]: ...
