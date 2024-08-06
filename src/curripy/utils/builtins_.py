from operator import methodcaller
def filter_(func):
    def caller(iterable):
        return filter(func, iterable)
    return caller

def map_(func):
    def caller(*iterables):
        return map(func, *iterables)

    return caller


call_method_values = methodcaller("values")
{"a":1}.values()