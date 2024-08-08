from ..__temporary.operator_ import is_ as is__, is_not as is_not_
from operator import call as call_
from ..utils import curry

is_ = curry(is__)
is_not = curry(is_not_)
call = curry(call_, arity=2)
