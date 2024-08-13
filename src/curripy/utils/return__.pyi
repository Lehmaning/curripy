from .curry_ import curry
from ..__generics import ReturnT

@curry
def return_(x: ReturnT, _) -> ReturnT: ...
