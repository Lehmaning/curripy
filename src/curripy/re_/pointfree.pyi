from typing import AnyStr, Callable
from re import Pattern, Match

def search(
    pattern: AnyStr | Pattern[AnyStr], flags: int = 0
) -> Callable[[str], Match[AnyStr]]: ...
