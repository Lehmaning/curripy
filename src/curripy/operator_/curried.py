import operator

from ..utils import curry
from ..__bootstrap.operator_ import is_, is_not, add, add_right, call, or_, getitem

__all__ = (
    "add",
    "add_right",
    "and_",
    "call",
    "concat",
    "contains",
    "countOf",
    "delitem",
    "eq",
    "floordiv",
    "ge",
    "getitem",
    "gt",
    "iadd",
    "iand",
    "iconcat",
    "ifloordiv",
    "ilshift",
    "imatmul",
    "imod",
    "imul",
    "indexOf",
    "ior",
    "ipow",
    "irshift",
    "is_",
    "is_not",
    "isub",
    "itruediv",
    "ixor",
    "le",
    "lshift",
    "lt",
    "matmul",
    "mod",
    "mul",
    "ne",
    "or_",
    "pow_",
    "rshift",
    "setitem",
    "sub",
    "truediv",
    "xor",
)

and_ = curry(operator.and_, arity=2)
concat = curry(operator.concat, arity=2)
contains = curry(operator.contains, arity=2)
countOf = curry(operator.countOf, arity=2)
delitem = curry(operator.delitem)
eq = curry(operator.eq, arity=2)
floordiv = curry(operator.floordiv, arity=2)
ge = curry(operator.ge, arity=2)
gt = curry(operator.gt, arity=2)
imod = curry(operator.imod, arity=2)
imul = curry(operator.imul, arity=2)
indexOf = curry(operator.indexOf, arity=2)
le = curry(operator.le, arity=2)
lshift = curry(operator.lshift, arity=2)
lt = curry(operator.lt, arity=2)
matmul = curry(operator.matmul, arity=2)
mod = curry(operator.mod, arity=2)
mul = curry(operator.mul, arity=2)
ne = curry(operator.ne, arity=2)
pow_ = curry(operator.pow)
rshift = curry(operator.rshift, arity=2)
setitem = curry(operator.setitem)
sub = curry(operator.sub, arity=2)
truediv = curry(operator.truediv, arity=2)
xor = curry(operator.xor, arity=2)

# Functions not exported by default
# mainly are impure functions
ixor = curry(operator.ixor, arity=2)
iadd = curry(operator.iadd, arity=2)
iand = curry(operator.iand, arity=2)
iconcat = curry(operator.iconcat, arity=2)
ifloordiv = curry(operator.ifloordiv, arity=2)
ilshift = curry(operator.ilshift, arity=2)
imatmul = curry(operator.imatmul, arity=2)
ior = curry(operator.ior, arity=2)
ipow = curry(operator.ipow, arity=2)
irshift = curry(operator.irshift, arity=2)
isub = curry(operator.isub, arity=2)
itruediv = curry(operator.itruediv, arity=2)
