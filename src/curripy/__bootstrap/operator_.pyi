from ..__temporary.operator_ import is_ as is__, is_not as is_not_
from ..utils import curry

is_ = curry(is__)
is_not = curry(is_not_)
