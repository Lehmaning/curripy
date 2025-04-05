from functools import lru_cache
from curripy._bootstrap.inspect_ import len_of_regular_args
from operator import add, or_
from curripy._overlays.operator_ import radd, add, or_

__all__ = ("curry", "curry_right")


def make_curry(
    process_args=add,
    process_kwargs=or_,  # use | to compose dict
):
    def currier(func=None, arity=None, *args, **kwargs):
        if func is None:
            @lru_cache(1024)
            def get_func(f):
                return currier(f, arity, *args, **kwargs)
            return get_func

        resolved_arity = len_of_regular_args(func) if arity is None else arity

        if len(args) >= resolved_arity:
            return func(*args, **kwargs)

        # @lru_cache(1024)
        def wrapper(*new_args, **new_kwargs):
            merged_args = process_args(args, new_args)
            merged_kwargs = process_kwargs(kwargs, new_kwargs)
            return currier(func, resolved_arity, *merged_args, **merged_kwargs)

        return wrapper

    return currier


curry = make_curry(add)
curry_right = make_curry(radd)
