def pass_arg_(arg, func, *args, **kwargs):
    return func(arg, *args, **kwargs)


def pass_arg(arg):
    def caller(func, *args, **kwargs):
        nonlocal arg
        return func(arg, *args, **kwargs)

    return caller
