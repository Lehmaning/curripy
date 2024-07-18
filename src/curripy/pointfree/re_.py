import re
from operator import methodcaller as m
from typing import Callable

from returns.maybe import Maybe, maybe

from ..functionalize_tools import partial


def search(pattern: str | re.Pattern[str], flags=0) -> Callable[[str], Maybe]:
    return maybe(partial(re.search, pattern, flags=flags))
