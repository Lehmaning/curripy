from ..__generics import ReturnT
from ..utils import return_
from ..__bootstrap.dummies import def_args_kwargs

def def_kwargs(**kwargs): ...
def def_args(*args): ...

return_true = return_(True)
return_false = return_(False)
return_1 = return_(1)
return_0 = return_(0)
