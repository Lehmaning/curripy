import re
from re import Pattern
from typing import AnyStr

__all__ = ["search"]

def search(
    pattern: str | Pattern[AnyStr], flags: int = 0
): ...