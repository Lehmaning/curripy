def is_(a):
    "Same as a is b."
    def __b(b):
        return a is b
    return __b


def is_not(a):
    "Same as a is b."
    def __b(b):
        return a is not b
    return __b
