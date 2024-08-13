def add(a):
    """
    >>> add(a)(b)

    Same as a + b.
    """

    def __b(b):
        nonlocal a
        return a + b

    return __b


def add_right(a):
    """
    >>> add_right(a)(b)

    Same as b + a.
    """

    def __b(b):
        nonlocal a
        return b + a

    return __b


def is_(a):
    """
    >>> is_(a)(b)

    Same as a is b.
    """

    def __b(b):
        nonlocal a
        return a is b

    return __b


def is_not(a):
    """
    >>> is_not(a)(b)

    Same as a is not b.
    """

    def __b(b):
        nonlocal a
        return a is not b

    return __b


def call(obj):
    "Same as obj(args, *args, **kwargs)."

    def caller(arg, /, *args, **kwargs):
        nonlocal obj
        return obj(arg, *args, **kwargs)

    return caller


def or_(a):
    """
    >>> or_(a)(b)

    Same as a | b.
    """

    def __b(b):
        nonlocal a
        return a | b

    return __b


def getitem(a):
    """
    >>> getitem(b)(a)

    Same as a[b].
    """

    def __b(b):
        nonlocal a
        return a[b]

    return __b
