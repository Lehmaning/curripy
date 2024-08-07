from ..__dummies.obj import obejct_ as __initial_missing

def reduce_generator(func, sequence, initial=__initial_missing):
    """
    This is a modified version of functools.reduce which returns a generator.
    To get the last result of the function, consider to use:
    >>> *_, x = reduce_generator(...)

    Apply a function of two arguments cumulatively to the items of a sequence
    or iterable, from left to right, so as to reduce the iterable to a single
    value.  For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates
    ((((1+2)+3)+4)+5).  If initial is present, it is placed before the items
    of the iterable in the calculation, and serves as a default when the
    iterable is empty.
    """
    it = iter(sequence)
    try:
        value = next(it) if initial is __initial_missing else initial
    except StopIteration:
        raise TypeError("reduce() of empty iterable with no initial value") from None
    else:
        for element in it:
            value = func(value, element)
            yield value
