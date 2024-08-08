import re
from ..utils import curry, partial

__all__ = ["search"]


fullmatch = curry(re.fullmatch)
sub = curry(re.sub)
search = curry(re.search)
match_ = curry(re.match)
subn = curry(re.subn)
