import operator
from types import MappingProxyType
from typing import (
    Any,
    Callable,
    Concatenate,
    Container,
    Hashable,
    Iterable,
    TypeGuard,
    TypeVar,
    overload,
)

from typing_extensions import TypeIs

from curripy.__generics import (
    ArgKwargP,
    ParamT,
    ParamT1,
    ParamT2,
    ParamTCon,
    ParamTCov,
    ReturnT,
    ReturnT1,
    ReturnT2,
    ReturnTCov,
)
from curripy.protocols import (
    SupportsAdd,
    SupportsContainsAndGetItem,
    SupportsLShift,
    SupportsOr,
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
HashableT1 = TypeVar("HashableT1", bound=Hashable)
HashableT2 = TypeVar("HashableT2", bound=Hashable)

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
def eq(a: ParamT, b: ParamT | object) -> TypeIs[ParamT]: ...
def contains(a: Container[object], b: ParamT) -> TypeGuard[Container[ParamT]]: ...

# @overload
# def or_(
#     a: MappingProxyType[HashableT1, ReturnT1], b: MappingProxyType[HashableT2, ReturnT2]
# ) -> MappingProxyType[HashableT1 | HashableT2, ReturnT1 | ReturnT2]: ...
# @overload
def or_(a: ParamT1, b: ParamT2) -> ParamT1 | ParamT2: ...

itemgetter = operator.itemgetter
methodcaller = operator.methodcaller
attrgetter = operator.attrgetter
