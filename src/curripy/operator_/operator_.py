from operator import call
from typing import Callable

from ..functionalize_tools import curry_right


pass_arg: Callable[..., Callable] = curry_right(call, arity=2)
