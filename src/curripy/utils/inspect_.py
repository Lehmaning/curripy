from inspect import Parameter, Signature, signature
from operator import itemgetter

from ..__bootstrap.builtins_ import filter_, values
from ..__temporary.functools_ import lru_cache
from ..__bootstrap.operator_ import is_, is_not
from ..dummies.func import def_args, def_kwargs
from .compose_ import pipe


def get_parameters(sig: Signature):
    return sig.parameters


def get_default(obj: Parameter):
    return obj.default


signature_parameters = lru_cache()(pipe(signature, get_parameters))

param_var_args: Parameter = lru_cache()(pipe(signature_parameters, itemgetter("args")))(
    def_args
)
param_var_kwargs: Parameter = lru_cache()(
    pipe(signature_parameters, itemgetter("kwargs"))
)(def_kwargs)

is_empty = is_(Signature.empty)
not_var_args = is_not(param_var_args)
not_var_kwargs = is_not(param_var_kwargs)

filter_out_var_args = filter_(not_var_args)
filter_out_var_kwargs = filter_(not_var_kwargs)

not_have_default = pipe(get_default, is_empty)
filter_out_default_params = filter_(not_have_default)

get_len_of_args = pipe(signature_parameters, len)
all_params = pipe(signature_parameters, values)
non_default_params = pipe(
    all_params,
    filter_out_default_params,
    filter_out_var_args,
    filter_out_var_kwargs,
    tuple,
)
len_of_non_default_params = lru_cache()(pipe(non_default_params, len))
