import operator

from ..__temporary import operator_ as operator_temporarily_typed
from ..utils import curry, curry_right

add = curry(operator_temporarily_typed.add, arity=2)
"""
>>> add(a)(b)

Same as a + b.
"""

radd = curry_right(operator_temporarily_typed.add, arity=2)
"""
>>> radd(a)(b)

Same as b + a.
"""

call = curry(operator.call, arity=2)
"""
>>> call(obj)(args, *args, **kwargs)

Same as obj(args, *args, **kwargs).
"""

is_ = curry(operator_temporarily_typed.is_, arity=2)
"""
>>> is_(a)(b)

Same as a is b.
"""

is_not = curry(operator_temporarily_typed.is_not, arity=2)
"""
>>> is_not(a)(b)

Same as a is not b.
"""

or_ = curry(operator.or_, arity=2)
"""
>>> or_(a)(b)

Same as a | b.
"""

getitem = curry_right(operator_temporarily_typed.getitem, arity=2)
"""
>>> getitem(b)(a)

Same as a[b].
"""
