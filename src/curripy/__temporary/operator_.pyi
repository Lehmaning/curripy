from ..__generics import ParamT
from typing import Any
from typing_extensions import TypeIs

def is_(a: Any, b: ParamT) -> TypeIs[ParamT]: ...
def is_not(a: ParamT, b: Any) -> TypeIs[ParamT]: ...
# TODO typeclass for eq