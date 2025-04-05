"""
Type stubs for currypy._bootstrap.operator_

Notice: curry and curry_right is for automtically type hinting, not original logic.
"""

import operator

from curripy._overlays import operator_ as operator_temporarily_typed
from curripy._overlays.operator_ import (
    attrgetter,
    itemgetter,
    methodcaller,
    pass_arg,
    argpasser,
)
from curripy.utils import curry, curry_right

__all__ = (
    # normal functions
    "add",
    "radd",
    "is_",
    "is_not",
    "or_",
    "contains",
    # new functions
    "pass_arg",
    "argpasser",
    "attrgetter",
    "itemgetter",
    "methodcaller",
    "radd",
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

contains = curry_right(operator_temporarily_typed.contains, arity=2)
in_ = curry(operator_temporarily_typed.contains, arity=2)
