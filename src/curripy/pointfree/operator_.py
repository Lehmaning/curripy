from operator import call

from ..functionalize_tools import curry_right

pass_arg = curry_right(call, arity=2)
