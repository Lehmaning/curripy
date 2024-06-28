from operator import methodcaller as m
from typing import Any, Callable
from collections import Counter


def most_common(n: int | None = None) -> Callable[[Counter], Any]:
    return m("most_common", n)
