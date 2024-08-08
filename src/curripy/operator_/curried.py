from operator import add as add_
from operator import and_ as and__
from operator import call as call_
from operator import concat as concat_
from operator import contains as contains_
from operator import countOf as countOf_
from operator import delitem as delitem_
from operator import eq as eq_
from operator import floordiv as floordiv_
from operator import ge as ge_
from operator import getitem as getitem_
from operator import gt as gt_
from operator import iadd as iadd_
from operator import iand as iand_
from operator import iconcat as iconcat_
from operator import ifloordiv as ifloordiv_
from operator import ilshift as ilshift_
from operator import imatmul as imatmul_
from operator import imod as imod_
from operator import imul as imul_
from operator import indexOf as indexOf_
from operator import ior as ior_
from operator import ipow as ipow_
from operator import irshift as irshift_
from operator import isub as isub_
from operator import itruediv as itruediv_
from operator import ixor as ixor_
from operator import le as le_
from operator import lshift as lshift_
from operator import lt as lt_
from operator import matmul as matmul_
from operator import mod as mod_
from operator import mul as mul_
from operator import ne as ne_
from operator import or_ as or__
from operator import pow as pow__
from operator import rshift as rshift_
from operator import setitem as setitem_
from operator import sub as sub_
from operator import truediv as truediv_
from operator import xor as xor_

from ..utils import curry
from ..__bootstrap.operator_ import is_ as is__
from ..__bootstrap.operator_ import is_not as is_not_

__all__ = [
    "add",
    "and_",
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
]


add = curry(add_)
and_ = curry(and__)
call = curry(call_, arity=2)
concat = curry(concat_)
contains = curry(contains_)
countOf = curry(countOf_)
delitem = curry(delitem_)
eq = curry(eq_)
floordiv = curry(floordiv_)
ge = curry(ge_)
getitem = curry(getitem_)
gt = curry(gt_)
iadd = curry(iadd_)
iand = curry(iand_)
iconcat = curry(iconcat_)
ifloordiv = curry(ifloordiv_)
ilshift = curry(ilshift_)
imatmul = curry(imatmul_)
imod = curry(imod_)
imul = curry(imul_)
indexOf = curry(indexOf_)
ior = curry(ior_)
ipow = curry(ipow_)
irshift = curry(irshift_)
is_ = curry(is__)
is_not = curry(is_not_)
isub = curry(isub_)
itruediv = curry(itruediv_)
ixor = curry(ixor_)
le = curry(le_)
lshift = curry(lshift_)
lt = curry(lt_)
matmul = curry(matmul_)
mod = curry(mod_)
mul = curry(mul_)
ne = curry(ne_)
or_ = curry(or__)
pow_ = curry(pow__)
rshift = curry(rshift_)
setitem = curry(setitem_)
sub = curry(sub_)
truediv = curry(truediv_)
xor = curry(xor_)
