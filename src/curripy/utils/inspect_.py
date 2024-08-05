from functools import lru_cache
from functools import partial as partial_
from inspect import Parameter, Signature, signature
from operator import is_, itemgetter, not_
from types import MappingProxyType
from typing import (
    Any,
)
from curripy.utils.compose_ import pipe
from curripy.utils.partial_ import partial

def call_method_values(d):
    return d.values()


def get_parameters(sig: Signature) -> MappingProxyType[str, Parameter]:
    return sig.parameters


def get_default(obj: Parameter) -> Any:
    return obj.default


def get_args(obj: partial_) -> tuple[Any]:
    return obj.args


def dummy(*args, **kwargs):
    pass


signature_parameters = lru_cache()(pipe(signature, get_parameters))

param_var_args: Parameter = pipe(signature_parameters, itemgetter("args"))(dummy)
param_var_kwargs: Parameter = pipe(signature_parameters, itemgetter("kwargs"))(dummy)
is_empty = partial(is_, Signature.empty)
not_var_args = pipe(partial(is_, param_var_args), not_)
not_var_kwargs = pipe(partial(is_, param_var_kwargs), not_)
not_have_default = pipe(get_default, is_empty)
filter_out_default_params = partial(filter, not_have_default)
filter_out_var_args = partial(filter, not_var_args)
filter_out_var_kwargs = partial(filter, not_var_kwargs)

get_len_of_args = lru_cache()(pipe(signature_parameters, len))
all_params = lru_cache()(pipe(signature_parameters, call_method_values))
non_default_params = pipe(
        all_params,
        filter_out_default_params,
        filter_out_var_args,
        filter_out_var_kwargs,
        tuple,
    )
len_of_non_default_params = lru_cache()(pipe(non_default_params, len))
