def pass_arg_(arg, func, *args, **kwargs):
    return func(arg, *args, **kwargs)


def pass_arg(arg):
    def __pass_arg(obj):
        return obj(arg)

    return __pass_arg