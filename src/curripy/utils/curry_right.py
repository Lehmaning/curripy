from curripy.utils.inspect_ import len_of_non_default_params
from curripy.utils.partial_ import partial

def curry_right(
    func,
    *args,
    arity=None,
    **kwargs,
):
    """
    Same as curry, but parameter receiveing order of the original func is right to left.
    """
    args = () if args is None else args
    kwargs = {} if kwargs is None else kwargs
    arity = len_of_non_default_params(func) if arity is None else arity
    if arity == 1:
        return func
    elif len(args) >= arity - 1:
        return partial(func, *reversed(args), **kwargs)
    elif arity > 1:
        def accepting_args(*passing_args, **passing_kwargs):
            nonlocal args
            nonlocal kwargs
            nonlocal func
            nonlocal arity
            apply_args = args + passing_args
            apply_kwargs = kwargs | passing_kwargs
            return curry_right(func, arity, *apply_args, **apply_kwargs)

        return accepting_args
    return func