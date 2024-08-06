from _collections_abc import ValuesView, dict_values
from typing import Callable, Iterable, Mapping, MutableMapping, TypeVar, overload

from typing_extensions import TypeIs

from ..__generics import ParamType, ParamType1, ParamType2
from ..utils import curry

KeyType = TypeVar("KeyType")
ValueType = TypeVar("ValueType")

@overload
def filter_(
    func: None,
) -> Callable[[Iterable[ParamType | None]], filter[ParamType]]:
    ...
@overload
def filter_(
    func: Callable[[ParamType2], TypeIs[ParamType1]]
) -> Callable[[Iterable[ParamType2]], filter[ParamType1]]: ...
@overload
def filter_(
    func: Callable[[ParamType], bool]
) -> Callable[[Iterable[ParamType]], filter]: ...

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
