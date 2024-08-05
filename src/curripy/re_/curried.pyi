from typing import Concatenate, ParamSpec, Match, AnyStr, Callable
from re import Pattern

P = ParamSpec("P")

search: Callable[Concatenate[AnyStr | Pattern[AnyStr], P], Callable[[str], Match]]