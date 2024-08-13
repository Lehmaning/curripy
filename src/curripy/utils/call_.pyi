from operator import attrgetter
from typing import Any, Callable, Concatenate

from ..__generics import ArgKwargP, ParamT, ReturnT
from ..utils.curry_ import curry

def pass_arg_(
    arg: ParamT,
    func: Callable[Concatenate[ParamT, ArgKwargP], ReturnT],
    *args: ArgKwargP.args,
    **kwargs: ArgKwargP.kwargs,
) -> ReturnT: ...

pass_arg = curry(pass_arg_, arity=2)

def methodcaller(name: str, *args, **kwargs) -> Callable[[Any], Any]: ...
