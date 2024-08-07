__all__ = ["tap"]


def tap(func):
    """
    To call the function and return its first argument instead of its result.
    It is a typing-improved version that is inspired by dry-python/returns.

    See also:
    - https://github.com/dry-python/returns/blob/66460df43ccda4ec8eeb95507f962e26cbb2c480/returns/functions.py#L53
    - https://x.com/joelnet/status/1165994838564777985

    Args:
        func (Callable[Concatenate[ParamType, P], None]): _description_

    Returns:
        Callable[Concatenate[ParamType, P], ParamType]: _description_
    """

    def caller(arg, **kwargs):
        nonlocal func
        func(arg, **kwargs)
        return arg

    return caller
