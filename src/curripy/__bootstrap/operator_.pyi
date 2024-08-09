from ..utils.curry_ import curry_right

from ..__temporary.operator_ import is_ as is__
from ..__temporary.operator_ import is_not as is_not_
import operator as o
from ..utils import curry

add = curry(o.add, arity=2)
"""
add(a)(b)

Same as a + b.
"""

add_right = curry_right(o.add, arity=2)
"""
add_right(a)(b)

Same as b + a.
"""

call = curry(o.call, arity=2)
"""
call(obj)(args, *args, **kwargs)

Same as obj(args, *args, **kwargs).
"""

is_ = curry(is__, arity=2)
"""
is_(a)(b)

Same as a is b.
"""

is_not = curry(is_not_, arity=2)
"""
is_not(a)(b)

Same as a is not b.
"""

or_ = curry(o.or_, arity=2)
"""
or_(a)(b)

Same as a | b.
"""

getitem = curry_right(o.getitem)
"""
getitem(b)(a)

Same as a[b].
"""
