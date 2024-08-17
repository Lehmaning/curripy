__all__ = (
    # normal functions
    "add",
    "radd",
    "is_",
    "is_not",
    "or_",
    "call",
    "getitem",
    # new functions
    "pass_arg_",
    "pass_arg",
    "attrgetter",
    "itemgetter",
    "methodcaller",
    "radd",
    "rsub",
)


def add(a):

    def __b(b):
        nonlocal a
        return a + b

    return __b


def radd(a):
    def __b(b):
        nonlocal a
        return b + a

    return __b


def contains(a):
    def __b(b):
        nonlocal a
        return b in a


def is_(a):
    def __b(b):
        nonlocal a
        return a is b

    return __b


def is_not(a):
    def __b(b):
        nonlocal a
        return a is not b

    return __b


def call(obj):
    def caller(arg, /, *args, **kwargs):
        nonlocal obj
        return obj(arg, *args, **kwargs)

    return caller


def or_(a):
    def __b(b):
        nonlocal a
        return a | b

    return __b


def getitem(a):
    def __b(b):
        nonlocal a
        return a[b]

    return __b


def pass_arg_(arg, func, *args, **kwargs):
    return func(arg, *args, **kwargs)


def pass_arg(arg):
    def caller(func, *args, **kwargs):
        nonlocal arg
        return func(arg, *args, **kwargs)

    return caller
