import re
from curripy.utils import curry

__all__ = []

def search(pattern, flags=0):
    return curry(re.search)(pattern, flags=flags)
