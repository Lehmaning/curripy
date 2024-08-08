from _collections_abc import ValuesView, dict_values
from typing import Any, Callable, Iterable, Mapping, MutableMapping, TypeVar, overload

from typing_extensions import TypeIs

from ..__generics import ParamT, ParamT1, ParamT2
from ..utils import curry

KeyType = TypeVar("KeyType")
ValueType = TypeVar("ValueType")

@overload
def filter_(
    func: None,
) -> Callable[[Iterable[ParamT | None]], filter[ParamT]]:
    ...
@overload
def filter_(
    func: Callable[[ParamT2], TypeIs[ParamT1]]
) -> Callable[[Iterable[ParamT2]], filter[ParamT1]]: ...
@overload
def filter_(
    func: Callable[[ParamT], Any]
) -> Callable[[Iterable[ParamT]], filter[Any]]: ...

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
