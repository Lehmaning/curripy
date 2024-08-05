__all__ = ["tap"]
def tap(
    func
):
    def caller(*args, **kwargs):
        nonlocal func
        func(*args, **kwargs)
        return args

    return caller
