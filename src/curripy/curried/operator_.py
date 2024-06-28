from operator import (
    abs,
    add,
    and_,
    call,
    concat,
    contains,
    countOf,
    delitem,
    eq,
    floordiv,
    ge,
    getitem,
    gt,
    iadd,
    iand,
    iconcat,
    ifloordiv,
    ilshift,
    imatmul,
    imod,
    imul,
    index,
    indexOf,
    inv,
    invert,
    ior,
    ipow,
    irshift,
    is_,
    is_not,
    isub,
    itruediv,
    ixor,
    le,
    length_hint,
    lshift,
    lt,
    matmul,
    mod,
    mul,
    ne,
    neg,
    not_,
    or_,
    pos,
    pow,
    rshift,
    setitem,
    sub,
    truediv,
    truth,
    xor,
)

from returns.curry import curry

__all__ = [
    "abs",
    "add",
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
    "index",
    "indexOf",
    "inv",
    "invert",
    "ior",
    "ipow",
    "irshift",
    "is_",
    "is_not",
    "isub",
    "itruediv",
    "ixor",
    "le",
    "length_hint",
    "lshift",
    "lt",
    "matmul",
    "mod",
    "mul",
    "ne",
    "neg",
    "not_",
    "or_",
    "pos",
    "pow",
    "rshift",
    "setitem",
    "sub",
    "truediv",
    "truth",
    "xor",
]
abs = curry(abs)
add = curry(add)
and_ = curry(and_)
call = curry(call)
concat = curry(concat)
contains = curry(contains)
countOf = curry(countOf)
delitem = curry(delitem)
eq = curry(eq)
floordiv = curry(floordiv)
ge = curry(ge)
getitem = curry(getitem)
gt = curry(gt)
iadd = curry(iadd)
iand = curry(iand)
iconcat = curry(iconcat)
ifloordiv = curry(ifloordiv)
ilshift = curry(ilshift)
imatmul = curry(imatmul)
imod = curry(imod)
imul = curry(imul)
index = curry(index)
indexOf = curry(indexOf)
inv = curry(inv)
invert = curry(invert)
ior = curry(ior)
ipow = curry(ipow)
irshift = curry(irshift)
is_ = curry(is_)
is_not = curry(is_not)
isub = curry(isub)
itruediv = curry(itruediv)
ixor = curry(ixor)
le = curry(le)
length_hint = curry(length_hint)
lshift = curry(lshift)
lt = curry(lt)
matmul = curry(matmul)
mod = curry(mod)
mul = curry(mul)
ne = curry(ne)
neg = curry(neg)
not_ = curry(not_)
or_ = curry(or_)
pos = curry(pos)
pow = curry(pow)
rshift = curry(rshift)
setitem = curry(setitem)
sub = curry(sub)
truediv = curry(truediv)
truth = curry(truth)
xor = curry(xor)
