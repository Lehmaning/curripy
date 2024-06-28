# %%
import re
from operator import methodcaller as m
from typing import Any, Callable

from returns.curry import curry, partial
from returns.maybe import Maybe, maybe
from returns.result import Result
from returns.pipeline import pipe
from curripy.pointfree.types import Splitable


def search(pattern: str | re.Pattern[str], flags=0) -> Callable[[str], Maybe]:
    return maybe(partial(re.search, pattern, flags=flags))


def groupdict(default) -> Callable:
    return m("groupdict", default)

def group(*groups) -> Callable:
    return m("group", *groups)

def split(pattern: Splitable, maxsplit: int=0):
    def split_(string):
    pattern.split()