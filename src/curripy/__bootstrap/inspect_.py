from inspect import Parameter, Signature, signature
from operator import contains

from curripy.__bootstrap.builtins_ import map_

from ..__overlays.functools_ import lru_cache
from .compose_ import pipe
from .builtins_ import filter_, keys, values
from .dummies import def_args_kwargs
from .operator_ import is_, is_not, itemgetter

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
param_var_args = pipe(signature_parameters, values, map_(get_name), filter_())(
    def_args_kwargs
)
"""Refers to the signature of positional varargs"""

param_var_kwargs = pipe(signature_parameters, itemgetter("kwargs"))(
    def_args_kwargs
)
"""Refers to the signature of keyword varargs"""

is_empty = is_(Signature.empty)
"""Check if a parameter has a default value"""

not_var_args = is_not(param_var_args)
not_var_kwargs = is_not(param_var_kwargs)
"""Check if a argument is *args or **kwargs"""

filter_out_var_args = filter_(not_var_args)
filter_out_var_kwargs = filter_(not_var_kwargs)

not_have_default = pipe(get_default, is_empty)
filter_out_optional_args = filter_(not_have_default)

get_len_of_args = pipe(signature_parameters, len)
all_params = pipe(signature_parameters, values)
non_default_params = lru_cache()(
    pipe(
        all_params,
        filter_out_optional_args,
        filter_out_var_args,
        filter_out_var_kwargs,
        tuple,
    )
)
len_of_non_default_params = pipe(non_default_params, len)
