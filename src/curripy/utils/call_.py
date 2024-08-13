def pass_arg_(arg, func, *args, **kwargs):
    return func(arg, *args, **kwargs)


def pass_arg(arg):
    def caller(func, *args, **kwargs):
        nonlocal arg
        return func(arg, *args, **kwargs)

    return caller


def attrgetter(name):
    def caller(obj):
        nonlocal name
        return getattr(obj, name)

    return caller


def methodcaller(name, *args, **kwargs):
    def caller(obj):
        nonlocal args, kwargs, name
        return attrgetter(name)(obj)(*args, **kwargs)

    return caller
