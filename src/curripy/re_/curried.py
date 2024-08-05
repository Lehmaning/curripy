import re
from curripy.utils import curry

__all__ = ["search"]


search = curry(re.search)