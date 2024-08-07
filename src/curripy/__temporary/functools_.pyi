from typing import final, Generic, Callable, Any
from functools import _CacheInfo
from ..__generics import ReturnType, P

@final
class _lru_cache_wrapper(Generic[P, ReturnType]):
    """
    Improved type hints of functools._lru_cache_wrapper, for temporary use

    - See:
      https://github.com/python/mypy/issues/5107#issuecomment-1355954910
    """

    def __call__(self, *args: P.args, **kwargs: P.kwargs) -> ReturnType: ...
    def cache_info(self) -> _CacheInfo: ...
    def cache_clear(self) -> None: ...
    def __copy__(self) -> _lru_cache_wrapper[P, ReturnType]: ...
    def __deepcopy__(self, __memo: Any) -> _lru_cache_wrapper[P, ReturnType]: ...

def lru_cache(
    maxsize: int | None = None,
) -> Callable[[Callable[P, ReturnType]], Callable[P, ReturnType]]:
    """
    Improved type hints of functools.lru_cache, for temporary use

    - See:
      https://github.com/python/mypy/issues/5107#issuecomment-1355954910
    """
    ...
