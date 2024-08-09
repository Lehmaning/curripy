from typing_extensions import TypeIs

from ..utils import curry

from ..__bootstrap.builtins_ import map_, filter_
from ..dummies.type import _ClassInfo

__all__ = (
    "divmod_",
    "map_",
    "filter_",
)

issubclass_ = curry(issubclass)
divmod_ = curry(divmod)

@curry
def isinstance_(
    obj: object,
    class_or_tuple: _ClassInfo,
) -> TypeIs[_ClassInfo]: ...

getattr_ = curry(getattr)
setattr_ = curry(setattr)
