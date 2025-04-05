from typing import Callable
from curripy.__generics import ParamT

def tap(
    func: Callable[[ParamT], None],
) -> Callable[[ParamT], ParamT]: ...
