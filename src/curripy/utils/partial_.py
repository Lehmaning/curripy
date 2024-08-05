from functools import partial as partial_

__all__ = ["partial"]


def partial_wrapper(
    func,
    *args,
    **kwargs,
):
    return partial_(func, *args, **kwargs)


def partial(func, *args, **kwargs):
    def apply(*passing_args, **passing_kwargs):
        nonlocal args
        nonlocal kwargs
        nonlocal func
        apply_args = args + passing_args
        apply_kwargs = kwargs | passing_kwargs
        return func(*apply_args, **apply_kwargs)

    return apply
