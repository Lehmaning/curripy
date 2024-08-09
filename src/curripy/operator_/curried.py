import operator as o

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

and_ = curry(o.and_, arity=2)
concat = curry(o.concat, arity=2)
contains = curry(o.contains, arity=2)
countOf = curry(o.countOf, arity=2)
delitem = curry(o.delitem)
eq = curry(o.eq, arity=2)
floordiv = curry(o.floordiv, arity=2)
ge = curry(o.ge, arity=2)
gt = curry(o.gt, arity=2)
iadd = curry(o.iadd, arity=2)
iand = curry(o.iand, arity=2)
iconcat = curry(o.iconcat, arity=2)
ifloordiv = curry(o.ifloordiv, arity=2)
ilshift = curry(o.ilshift, arity=2)
imatmul = curry(o.imatmul, arity=2)
imod = curry(o.imod, arity=2)
imul = curry(o.imul, arity=2)
indexOf = curry(o.indexOf, arity=2)
ior = curry(o.ior, arity=2)
ipow = curry(o.ipow, arity=2)
irshift = curry(o.irshift, arity=2)
isub = curry(o.isub, arity=2)
itruediv = curry(o.itruediv, arity=2)
ixor = curry(o.ixor, arity=2)
le = curry(o.le, arity=2)
lshift = curry(o.lshift, arity=2)
lt = curry(o.lt, arity=2)
matmul = curry(o.matmul, arity=2)
mod = curry(o.mod, arity=2)
mul = curry(o.mul, arity=2)
ne = curry(o.ne, arity=2)
pow_ = curry(o.pow)
rshift = curry(o.rshift, arity=2)
setitem = curry(o.setitem)
sub = curry(o.sub, arity=2)
truediv = curry(o.truediv, arity=2)
xor = curry(o.xor, arity=2)
