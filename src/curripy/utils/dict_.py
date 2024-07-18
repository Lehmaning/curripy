from typing import Callable, Iterable, Sequence

from ..curried.builtins_ import map_
from ..functionalize_tools import curry_ as curry
from ..functionalize_tools import partial, pipe


@curry
def map_zip(
    mapper_func: Callable[[Iterable], Iterable],
    keys: Iterable,
) -> dict:
    values = map(mapper_func, keys)
    return zip(keys, values)
