from typing import Any, Protocol

from _typeshed import (
    SupportsAdd,
    SupportsContainsAndGetItem,
    SupportsSub,
    SupportsRAdd,
    SupportsRSub,
)
from typing_extensions import TypeIs

from curripy.utils.curry_ import curry_right

from ..__generics import (
    ParamT,
    ParamTCon,
    ParamTCov,
    ReturnTCov,
)

__all__ = (
    "is_",
    "is_not",
    "add",
    "sub",
    "rshift",
    # new functions
    "radd",
    "rsub",
)

class SupportsRShift(Protocol[ParamTCon, ParamTCov]):
    def __rshift__(self, x: ParamTCon, /) -> ParamTCov: ...

def is_(a: ParamT, b: Any) -> TypeIs[ParamT]: ...
def is_not(a: Any, b: ParamT) -> TypeIs[ParamT]: ...
def add(a: SupportsAdd[ParamTCon, ParamTCov], b: ParamTCov) -> ParamTCov: ...
def radd(a: SupportsRAdd[ParamTCon, ParamTCov], b: ParamTCon) -> ParamTCov: ...
def getitem(
    a: SupportsContainsAndGetItem[ParamTCon, ReturnTCov], b: ParamTCon
) -> ReturnTCov: ...
def sub(a: SupportsSub[ParamTCon, ParamTCov], b: ParamTCon) -> ParamTCov: ...
def rsub(a: SupportsRSub[ParamTCon, ParamTCov], b: ParamTCon) -> ParamTCov: ...
def rshift(a: SupportsRShift[ParamTCon, ParamTCov], b: ParamTCon) -> ParamTCov: ...
def attrgetter(name: str):
    def caller(obj: object):
        nonlocal name
        return getattr(obj, name)
    return caller

def methodcaller(name: str, *args, **kwargs):
    def caller(obj: object):
        nonlocal args, kwargs, name
        return getattr(obj, name)(*args, **kwargs)
    return caller

itemgetter = curry_right(getitem, arity=2)
