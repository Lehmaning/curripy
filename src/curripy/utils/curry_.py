from ..__bootstrap.inspect_ import len_of_regular_args
from ..__bootstrap.operator_ import or_, radd, add

__all__ = ("curry", "curry_right")


def make_curry(
    process_args=add,
    process_kwargs=or_, # use | to compose dict
):
    def currier(*args, func=None, arity=None, **kwargs):
        if func is None:
            return lambda f: currier(f, arity, *args, **kwargs)

        resolved_arity = len_of_regular_args(func) if arity is None else arity

        if len(args) == resolved_arity:
            return func(*args, **kwargs)
        elif len(args) > resolved_arity:
            raise ValueError("Too much arguments.")

        def wrapper(*new_args, **new_kwargs):
            if len(new_args) <= 0:
                raise ValueError("Arguments needed.")
            merged_args = process_args(args)(new_args)
            merged_kwargs = process_kwargs(kwargs)(new_kwargs)
            return currier(func, resolved_arity, *merged_args, **merged_kwargs)

        return wrapper

    return currier


curry = make_curry(add)
curry_right = make_curry(radd)
