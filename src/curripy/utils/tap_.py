__all__ = ["tap"]


def tap(func):
    def caller(arg, **kwargs):
        nonlocal func
        func(arg, **kwargs)
        return arg

    return caller
