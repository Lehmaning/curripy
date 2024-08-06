from typing import (
    TypeVar,
    MutableMapping,
    overload,
    Mapping,
)
from _collections_abc import ValuesView, dict_values
from ..utils import curry

KeyType = TypeVar("KeyType")
ValueType = TypeVar("ValueType")

filter_ = curry(filter)
map_ = curry(map)

@overload
def call_method_values(
    d: dict[KeyType, ValueType],
) -> dict_values[KeyType, ValueType]: ...
@overload
def call_method_values(
    d: MutableMapping[KeyType, ValueType],
) -> ValuesView[ValueType]: ...
@overload
def call_method_values(d: Mapping[KeyType, ValueType]) -> ValuesView[ValueType]: ...
