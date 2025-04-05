from inspect import Parameter, Signature, signature
from operator import not_

from curripy._overlays.functools_ import lru_cache

from .builtins_ import filter_, values
from .compose import compose, pipe
from .operator_ import contains, is_

__all__ = ("signature_parameters", "get_regular_args")


# defining getters
def get_parameters(sig: Signature):
    return sig.parameters


def get_default(obj: Parameter):
    return obj.default


def get_name(obj: Parameter):
    return obj.name


# base function
signature_parameters = lru_cache()(pipe(signature, get_parameters))
"""Get parameters from the signature of the function"""

# get Parameter of args and kwargs
not_contains_asterisk = compose(not_, contains("*"))
"""Check if any ParamSpec exists"""
not_var_args = pipe(get_name, not_contains_asterisk)
"""Check if an argument is *args or **kwargs"""

empty = Signature.empty
"""Check if an argument has no default value"""
not_have_default = pipe(get_default, is_(empty))
"""Check if an argument has a default value"""

filter_out_var_args = filter_(not_var_args)
filter_out_optional_args = filter_(not_have_default)

all_params = pipe(signature_parameters, values)
"""Get mapping of types to arguments from a callable object"""
get_regular_args = lru_cache(maxsize=1024)(
    pipe(
        all_params,
        filter_out_var_args,
        filter_out_optional_args,
        tuple,
    )
)
"""Get list of arguments from function"""
len_of_args = pipe(signature_parameters, len)
len_of_regular_args = pipe(get_regular_args, len)
