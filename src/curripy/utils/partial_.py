__all__ = ("partial",)


def partial(func, *args, **kwargs):
    def caller(*passing_args, **passing_kwargs):
        nonlocal args
        nonlocal kwargs
        nonlocal func
        apply_args = args + passing_args
        apply_kwargs = kwargs | passing_kwargs
        return func(*apply_args, **apply_kwargs)

    return caller
