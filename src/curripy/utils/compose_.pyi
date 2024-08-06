from typing import TypeAlias, ParamSpec, Callable, TypeVar, overload, Union

P = ParamSpec("P")
ArgumentType = TypeVar("ArgumentType")
ReturnType1 = TypeVar("ReturnType1")
ReturnType2 = TypeVar("ReturnType2")
ReturnType3 = TypeVar("ReturnType3")
ReturnType4 = TypeVar("ReturnType4")
ReturnType5 = TypeVar("ReturnType5")

@overload
def pipe(
    func1: Callable[P, ReturnType1],
) -> Callable[P, ReturnType1]: ...
@overload
def pipe(
    func1: Callable[[ArgumentType], ReturnType2],
    func2: Callable[[ReturnType2], ReturnType1],
) -> Callable[[ArgumentType], ReturnType1]: ...
@overload
def pipe(
    func1: Callable[[ArgumentType], ReturnType2],
    func2: Callable[[ReturnType2], ReturnType3],
    func3: Callable[[ReturnType3], ReturnType1],
) -> Callable[[ArgumentType], ReturnType1]: ...
@overload
def pipe(
    func1: Callable[[ArgumentType], ReturnType2],
    func2: Callable[[ReturnType2], ReturnType3],
    func3: Callable[[ReturnType3], ReturnType4],
    func4: Callable[[ReturnType4], ReturnType1],
) -> Callable[[ArgumentType], ReturnType1]: ...
@overload
def pipe(
    func1: Callable[[ArgumentType], ReturnType2],
    func2: Callable[[ReturnType2], ReturnType3],
    func3: Callable[[ReturnType3], ReturnType4],
    func4: Callable[[ReturnType4], ReturnType5],
    func5: Callable[[ReturnType5], ReturnType1],
) -> Callable[[ArgumentType], ReturnType1]: ...
@overload
def compose(
    func1: Callable[[ArgumentType], ReturnType1],
) -> Callable[[ArgumentType], ReturnType1]: ...
@overload
def compose(
    func2: Callable[[ReturnType2], ReturnType1],
    func1: Callable[[ArgumentType], ReturnType2],
) -> Callable[[ArgumentType], ReturnType1]: ...
@overload
def compose(
    func3: Callable[[ReturnType3], ReturnType1],
    func2: Callable[[ReturnType2], ReturnType3],
    func1: Callable[[ArgumentType], ReturnType2],
) -> Callable[[ArgumentType], ReturnType1]: ...
@overload
def compose(
    func4: Callable[[ReturnType4], ReturnType1],
    func3: Callable[[ReturnType3], ReturnType4],
    func2: Callable[[ReturnType2], ReturnType3],
    func1: Callable[[ArgumentType], ReturnType2],
) -> Callable[[ArgumentType], ReturnType1]: ...
@overload
def compose(
    func5: Callable[[ReturnType5], ReturnType1],
    func4: Callable[[ReturnType4], ReturnType5],
    func3: Callable[[ReturnType3], ReturnType4],
    func2: Callable[[ReturnType2], ReturnType3],
    func1: Callable[[ArgumentType], ReturnType2],
) -> Callable[[ArgumentType], ReturnType1]: ...
