import re
from ..functionalize_tools import partial


def search(pattern, flags=0):
    return partial(re.search, pattern, flags=flags)
