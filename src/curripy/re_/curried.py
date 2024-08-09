import re
from ..utils import curry

__all__ = (
    "findall",
    "finditer",
    "fullmatch",
    "match_",
    "search",
    "split",
    "sub",
    "subn",
)

findall = curry(re.findall)
finditer = curry(re.finditer)
fullmatch = curry(re.fullmatch)
match_ = curry(re.match)
search = curry(re.search)
split = curry(re.split)
sub = curry(re.sub)
subn = curry(re.subn)
