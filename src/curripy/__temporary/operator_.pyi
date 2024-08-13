from ..__generics import ParamT, ParamT1, ParamT2, ReturnT
from typing import Any
from typing_extensions import TypeIs
from _typeshed import SupportsAdd, SupportsContainsAndGetItem

def is_(a: Any, b: ParamT) -> TypeIs[ParamT]: ...
def is_not(a: ParamT, b: Any) -> TypeIs[ParamT]: ...
def add(a: SupportsAdd[ParamT1, ParamT2], b: ParamT1) -> ParamT2: ...
def getitem(a: SupportsContainsAndGetItem[ParamT, ReturnT], b: ParamT) -> ReturnT: ...
