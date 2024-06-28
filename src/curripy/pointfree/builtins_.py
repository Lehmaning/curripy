# from returns.curry import curry
from pydash import curry_right

isinstance_ = curry_right(isinstance, arity=2)