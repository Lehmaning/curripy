from typing import Concatenate, Callable
from ..__generics import ParamType, P

def tap(
    func: Callable[Concatenate[ParamType, P], None],
) -> Callable[Concatenate[ParamType, P], ParamType]:
    """
    To call the function and return its first argument instead of its result.
    It is a typing-improved version that is inspired by dry-python/returns.

    See also:
    - https://github.com/dry-python/returns/blob/66460df43ccda4ec8eeb95507f962e26cbb2c480/returns/functions.py#L53
    - https://xcancel.com/joelnet/status/1165994838564777985

    Args:
        func (Callable[Concatenate[ParamType, P], None]): _description_

    Returns:
        Callable[Concatenate[ParamType, P], ParamType]: _description_
    """
    ...
