from functools import lru_cache
from inspect import Parameter, Signature, signature
from operator import is_not, itemgetter

from .builtins_ import call_method_values, filter_
from .compose_ import pipe
from .operator_ import is_
from .partial_ import partial


def get_parameters(sig: Signature):
    return sig.parameters


def get_default(obj: Parameter):
    return obj.default


def dummy(*args, **kwargs):
    pass

signature_parameters = lru_cache()(pipe(signature, get_parameters))

param_var_args: Parameter = pipe(signature_parameters, itemgetter("args"))(dummy)
param_var_kwargs: Parameter = pipe(signature_parameters, itemgetter("kwargs"))(dummy)

is_empty = partial(is_, Signature.empty)
not_var_args = partial(is_not, param_var_args)
not_var_kwargs = partial(is_not, param_var_kwargs)

filter_out_var_args = filter_(not_var_args)
filter_out_var_kwargs = filter_(not_var_kwargs)

not_have_default = pipe(get_default, is_empty)
filter_out_default_params = filter_( not_have_default)

get_len_of_args = pipe(signature_parameters, len)
all_params = pipe(signature_parameters, call_method_values)
non_default_params = pipe(
        all_params,
        filter_out_default_params,
        filter_out_var_args,
        filter_out_var_kwargs,
        tuple,
    )
len_of_non_default_params = lru_cache()(pipe(non_default_params, len))
