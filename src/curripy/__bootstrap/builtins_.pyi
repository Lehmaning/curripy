from _collections_abc import ValuesView, dict_values
from typing import Any, Any, Callable, Iterable, Mapping, MutableMapping, TypeVar, overload

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
    func: Callable[[ParamType], Any]
) -> Callable[[Iterable[ParamType]], filter[Any]]: ...

map_ = curry(map)

@overload
def values(
    d: dict[KeyType, ValueType],
) -> dict_values[KeyType, ValueType]: ...
@overload
def values(
    d: MutableMapping[KeyType, ValueType],
) -> ValuesView[ValueType]: ...
@overload
def values(d: Mapping[KeyType, ValueType]) -> ValuesView[ValueType]: ...
