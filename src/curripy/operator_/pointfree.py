from ..utils import curry

__all__ = [
    "pass_arg",
]

@curry
def pass_arg(arg, obj, *args, **kwargs):
    """Same as obj(arg)."""
    return obj(arg, *args, **kwargs)

