import operator
from typing import (
    Any,
    Callable,
    Concatenate,
    Container,
    TypeGuard,
)

from typing_extensions import TypeIs


from ..__generics import (
    ArgKwargP,
    ParamT,
    ParamTCon,
    ReturnT,
    ReturnTCov,
)
from ..protocols import (
    SupportsAdd,
    SupportsContainsAndGetItem,
    SupportsLShift,
    # SupportsOr,
    SupportsRAdd,
    SupportsRShift,
    SupportsRSub,
    SupportsSub,
)

__all__ = (
    "is_",
    "is_not",
    "add",
    "sub",
    "contains",
    "rshift",
    "lshift",
    "getitem",
    # "or_",
    "itemgetter",
    "methodcaller",
    "attrgetter",
    # new functions
    "radd",
    "rsub",
    "argpasser",
    "pass_arg",
)

# def or_(a: SupportsOr[ParamTCon, ReturnTCov], b: ParamTCon) -> ReturnTCov: ...
def is_(a: ParamT, b: Any) -> TypeIs[ParamT]: ...
def is_not(a: Any, b: ParamT) -> TypeIs[ParamT]: ...
def add(a: SupportsAdd[ParamTCon, ReturnTCov], b: ParamTCon) -> ReturnTCov: ...
def radd(a: SupportsRAdd[ParamTCon, ReturnTCov], b: ParamTCon) -> ReturnTCov: ...
def sub(a: SupportsSub[ParamTCon, ReturnTCov], b: ParamTCon) -> ReturnTCov: ...
def rsub(a: SupportsRSub[ParamTCon, ReturnTCov], b: ParamTCon) -> ReturnTCov: ...
def rshift(a: SupportsRShift[ParamTCon, ReturnTCov], b: ParamTCon) -> ReturnTCov: ...
def lshift(a: SupportsLShift[ParamTCon, ReturnTCov], b: ParamTCon) -> ReturnTCov: ...
def getitem(
    a: SupportsContainsAndGetItem[ParamTCon, ReturnTCov], b: ParamTCon
) -> ReturnTCov: ...
def pass_arg(
    arg: ParamT,
    func: Callable[Concatenate[ParamT, ArgKwargP], ReturnT],
    *args: ArgKwargP.args,
    **kwargs: ArgKwargP.kwargs,
) -> ReturnT: ...
def argpasser(
    arg: ParamT,
) -> Callable[
    [Callable[[ParamT], ReturnT]],
    ReturnT,
]: ...
def contains(a: Container[Any], b: ParamT) -> TypeGuard[ParamT]: ...

itemgetter = operator.itemgetter
methodcaller = operator.methodcaller
attrgetter = operator.attrgetter
