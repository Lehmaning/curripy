def pass_arg_(arg, func, *args, **kwargs):
    return func(arg, *args, **kwargs)


def pass_arg(arg):
    def caller(func):
        nonlocal arg
        return func(arg)

    return caller
