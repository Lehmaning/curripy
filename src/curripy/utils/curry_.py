from ..__bootstrap.inspect_ import len_of_non_default_params
from ..__bootstrap.operator_ import or_, add_right, add

__all__ = (
    "curry",
    "curry_right",
)


def merge_args(recurser, func, process_args_func, process_kwargs_func, arity):
    def caller(*passing_args, **passing_kwargs):
        nonlocal recurser, func, process_args_func, process_kwargs_func, arity
        apply_args = process_args_func(passing_args)
        apply_kwargs = process_kwargs_func(passing_kwargs)
        return recurser(func, arity, *apply_args, **apply_kwargs)

    return caller


def curry_decorator(
    curry_func, process_args_func_base, process_kwargs_func_base, arity=None
):
    def init_args(func, *args, **kwargs):
        nonlocal process_args_func_base, process_kwargs_func_base, arity
        __args = () if args is None else args
        __kwargs = {} if kwargs is None else kwargs
        __arity: int = len_of_non_default_params(func) if arity is None else arity
        return merge_args(
            curry_func,
            func,
            process_args_func_base(__args),
            process_kwargs_func_base(__kwargs),
            __arity,
        )

    return init_args


def curry(
    func=None,
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
    if func is None:
        return curry_decorator(curry, add, or_, arity=arity)
    elif arity is None:
        return curry_decorator(curry, add, or_, arity=arity)(func, *args, **kwargs)
    if arity == 1:
        return func
    if len(args) >= arity:
        return func(*args, **kwargs)
    if arity > 1:
        return merge_args(
            curry,
            func,
            add(args),
            or_(kwargs),
            arity,
        )
    return func


def curry_right(
    func=None,
    arity=None,
    *args,
    **kwargs,
):
    if func is None:
        return curry_decorator(curry_right, add_right, or_, arity)
    elif arity is None:
        return curry_decorator(curry_right, add_right, or_)(func)
    if arity == 1:
        return func
    if len(args) >= arity:
        return func(*args, **kwargs)
    if arity > 1:
        return merge_args(
            curry_right,
            func,
            add_right(args),
            or_(kwargs),
            arity,
        )
    return func
