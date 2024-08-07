from ..__generics import ParamType
from typing import Any
from typing_extensions import TypeIs

def is_(a: Any, b: ParamType) -> TypeIs[ParamType]: ...
def is_not(a: ParamType, b: Any) -> TypeIs[ParamType]: ...