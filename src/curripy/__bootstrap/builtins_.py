from operator import methodcaller

__all__ = (
    "filter_",
    "map_",
    "values",
)


def filter_(func):
    def caller(iterable):
        return filter(func, iterable)

    return caller


def map_(func):
    def caller(*iterables):
        return map(func, *iterables)

    return caller


values = methodcaller("values")
