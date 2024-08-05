def filter_(func):
    def caller(iterable):
        return filter(func, iterable)
    return caller

def map_(func):
    def caller(*iterables):
        return map(func, *iterables)

    return caller