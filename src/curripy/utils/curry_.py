from .inspect_ import len_of_non_default_params
from .partial_ import partial


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
    __args = () if args is None else args
    __kwargs = {} if kwargs is None else kwargs
    __arity: int = len_of_non_default_params(func) if arity is None else arity
    if __arity == 1:
        return func
    if len(__args) >= __arity - 1:
        return partial(func, *args, **kwargs)
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
    return curry(
        func,
        arity=arity,
        *reversed(args),
        **kwargs,
    )
