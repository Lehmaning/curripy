from ..functionalize_tools import curry_right

isinstance_ = curry_right(isinstance, arity=2)
issubclass_ = curry_right(isinstance, arity=2)
