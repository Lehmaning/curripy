from .inspect_ import len_of_non_default_params

__all__ = [
    "curry",
    "curry_right",
]


def curry(
    func,
    arity=None,
    *args,
    **kwargs,
):
    """
    This function gets arguments recursively, and call the passed function after being received enough positional arguments which have the same amount of the arity.
    Currently any keywords arguments will be overwritten by keywords newly passed in any generation of curried function.

    Args:
        func (Callable[ArgumentType, ReturnT]): the function to be curried.
        arity (int | None, optional): max number of arguments to be passed. Defaults to None.

    Returns:
        Callable | ReturnT: a partial applied function or final return of the function
    """
    __args = () if args is None else args
    __kwargs = {} if kwargs is None else kwargs
    __arity: int = len_of_non_default_params(func) if arity is None else arity
    if __arity == 1:
        return func
    if len(__args) >= __arity:
        return func(*args, **kwargs)
    if __arity > 1:

        def accepting_args(*passing_args, **passing_kwargs):
            nonlocal __args
            nonlocal __kwargs
            nonlocal __arity
            nonlocal func
            apply_args = __args + passing_args
            apply_kwargs = __kwargs | passing_kwargs
            return curry(func, __arity, *apply_args, **apply_kwargs)

        return accepting_args
    return func


def curry_right(
    func,
    arity=None,
    *args,
    **kwargs,
):
    __args = () if args is None else args
    __kwargs = {} if kwargs is None else kwargs
    __arity: int = len_of_non_default_params(func) if arity is None else arity
    if __arity == 1:
        return func
    if len(__args) >= __arity:
        return func(*args, **kwargs)
    if __arity > 1:

        def accepting_args(*passing_args, **passing_kwargs):
            nonlocal __args
            nonlocal __kwargs
            nonlocal __arity
            nonlocal func
            apply_args = passing_args + __args
            apply_kwargs = __kwargs | passing_kwargs
            return curry_right(func, __arity, *apply_args, **apply_kwargs)

        return accepting_args
    return func
