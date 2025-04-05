import re

from curripy.utils.curry import curry_right
from curripy.utils import curry

__all__ = ()

# functions not exported to root package
findall = curry(re.findall)
finditer = curry(re.finditer)
fullmatch = curry(re.fullmatch)
match_ = curry(re.match)
search = curry(re.search)
sub = curry(re.sub)
subn = curry(re.subn)
split = curry(re.split, arity=2)
