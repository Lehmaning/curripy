"""
This module is used for code refactoring or experiments on new feature.
"""

from .inspect_ import len_of_non_default_params

__all__ = ["curry"]


def partial(func, *args, **kwargs):
    def apply(*passing_args, **passing_kwargs):
        nonlocal args
        nonlocal kwargs
        nonlocal func
        apply_args = args + passing_args
        apply_kwargs = kwargs | passing_kwargs
        return func(*apply_args, **apply_kwargs)
    return apply

def curry(
    func,
    arity=None,
    *args,
    **kwargs,
):
    """
    Getting arguments recursively.
    Call the function after being received positional arguments which have the same amount of arity.
    Currently any keywords arguments will be overwritten by keywords newly passed in any generation of curried function
    This function has issues in type support, please avoid to use it in production.

    Args:
        func (Callable[ArgumentType, ReturnType]): the function to be curried.
        arity (int | None, optional): max number of arguments to be passed. Defaults to None.

    Returns:
        Callable | ReturnType: _description_
    """
    args = () if args is None else args
    kwargs = {} if kwargs is None else kwargs
    arity = len_of_non_default_params(func) if arity is None else arity
    if len(args) >= arity - 1:
        return partial(func, *args, **kwargs)
    if arity > 1:

        def accepting_args(*passing_args, **passing_kwargs):
            nonlocal args
            nonlocal kwargs
            nonlocal func
            nonlocal arity
            apply_args = args + passing_args
            apply_kwargs = kwargs | passing_kwargs
            return curry(func, arity, *apply_args, **apply_kwargs)

        return accepting_args
    return func
