"""
Type stubs for currypy.__bootstrap.operator_

Notice: curry and curry_right is for automtically type hinting, not original logic.
"""

import operator
from typing import Any, Callable, Concatenate

from ..__generics import ArgKwargP, ParamT, ReturnT
from ..__overlays import operator_ as operator_temporarily_typed
from ..utils import curry, curry_right

__all__ = (
    # normal functions
    "add",
    "radd",
    "is_",
    "is_not",
    "or_",
    "call",
    "getitem",
    # pointfree style functions
    "pass_arg_",
    "pass_arg",
    "attrgetter",
    "itemgetter",
    "methodcaller",
)

add = curry(operator_temporarily_typed.add, arity=2)
"""
>>> add(a)(b)

Same as a + b
"""

radd = curry_right(operator_temporarily_typed.add, arity=2)
"""
>>> radd(a)(b)

Same as b + a
"""

call = curry(operator.call, arity=2)
"""
>>> call(obj)(args, *args, **kwargs)

Same as obj(args, *args, **kwargs)
"""

is_ = curry(operator_temporarily_typed.is_, arity=2)
"""
>>> is_(a)(b)

Same as a is b
"""

is_not = curry(operator_temporarily_typed.is_not, arity=2)
"""
>>> is_not(a)(b)

Same as a is not b
"""

or_ = curry(operator.or_, arity=2)
"""
>>> or_(a)(b)

Same as a | b
"""

getitem = curry(operator_temporarily_typed.getitem, arity=2)
"""
>>> getitem(b)(a)

Same as a[b]
"""

def pass_arg_(
    arg: ParamT,
    func: Callable[Concatenate[ParamT, ArgKwargP], ReturnT],
    *args: ArgKwargP.args,
    **kwargs: ArgKwargP.kwargs,
) -> ReturnT: ...
def methodcaller(name: str, *args, **kwargs) -> Callable[[Any], Any]: ...
def attrgetter(name: str) -> Callable[[Any], Any]: ...
itemgetter = curry_right(operator_temporarily_typed.getitem, arity=2)
pass_arg = curry(pass_arg_, arity=2)
