import re
from typing import AnyStr, Callable
from ...functionalize_tools import partial


def search(
    pattern: AnyStr | re.Pattern[AnyStr], flags=0
) -> Callable[[str], re.Match[AnyStr] | None]:
    return partial(re.search, pattern, flags=flags)
