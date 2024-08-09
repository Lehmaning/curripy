"""
Attention: This module is not in use. Just written for experiments.
"""

from enum import IntEnum
from typing import (
    overload,
    Callable,
    Generic,
)

from curripy.utils.inspect_ import len_of_non_default_params
from ..__generics import ParamT1, ParamT2,ParamT3, ParamT4, ParamT5, ReturnT, ArgKwargP

__all__ = ("curry")

class Order(IntEnum):
    LeftToRight = 0
    RightToLeft = 1


class Curry(Generic[ParamT1, ReturnT, ArgKwargP]):
    """
    Getting arguments recursively.
    Call the function after being received positional arguments which have the same amount of arity.
    Currently any keywords arguments will overwrite ones of the same name passed before,
    so it is better to pass all the keyword and optional arguments at the first call or the last.
    Also, this class can serve as a "partial function".

    Attributes:
        func (Callable[ArgKwargP, ReturnT]): the function to be curried
        arity (int | None, optional): max number of arguments to be passed, default is the amount of required parameters
    """
    __slots__ = ("func", "arity", "__args", "__kwargs", "__call_count", "__order")
    def __init__(
        self,
        func: Callable[ArgKwargP, ReturnT],
        arity: int | None = None,
        order: int = Order.LeftToRight,
    ) -> None:
        self.func = func
        self.arity = len_of_non_default_params(self.func) if arity is None else arity
        self.__args = ()
        self.__kwargs = {}
        self.__call_count = 0
        self.__order = order

    def __call__(self, *args, **kwargs):
        args = (
            self.__args + args
            if self.__order is Order.LeftToRight
            else args + self.__args
        )
        kwargs = self.__kwargs | kwargs
        if self.__call_count + 1 >= self.arity or self.arity <= 1:
            return self.call(self.func, *args, **kwargs)
        return (
            self.__class__(
                self.func,
                self.arity,
            )
            .__set_args(*args)
            .__set_kwargs(**kwargs)
            .__set_call_count(self.__call_count + len(args))
        )

    @staticmethod
    def call(
        func: Callable[ArgKwargP, ReturnT], *args: ArgKwargP.args, **kwargs: ArgKwargP.kwargs
    ) -> ReturnT:
        """
        A function same as operator.call with generic type support, limited with the Curry class

        Args:
            func (Callable[ArgKwargP, ReturnT]): the function to be called

        Returns:
            ReturnT: the return type of the func
        """
        return func(*args, **kwargs)

    def __repr__(self) -> str:
        return "<{} {} {} {}>".format(
            self.__class__.__name__, self.func.__name__, self.__args, self.__kwargs
        )

    def __set_args(self, *args):
        self.__args = tuple(args)
        return self

    def __set_kwargs(self, **kwargs):
        self.__kwargs = dict(kwargs)
        return self

    def __set_call_count(self, call_count: int):
        self.__call_count = call_count
        return self


class Curry1(Curry[ParamT1, ReturnT, ArgKwargP]):
    def __call__(self, arg1: ParamT1, **kwargs) -> ReturnT:
        return super().__call__(arg1, **kwargs)


class Curry2(Curry[ParamT1, Curry1[ParamT2, ReturnT, ArgKwargP], ArgKwargP]):
    @overload
    def __call__(
        self, arg1: ParamT1, **kwargs
    ) -> Curry1[ParamT2, ReturnT, ArgKwargP]: ...
    @overload
    def __call__(self, arg1: ParamT1, arg2: ParamT2, **kwargs) -> ReturnT: ...
    def __call__(self, *args, **kwargs):
        return super().__call__(*args, **kwargs)


class Curry3(Curry[ParamT1, Curry2[ParamT2, ParamT3, ReturnT, ArgKwargP], ArgKwargP]):
    @overload
    def __call__(
        self, arg1: ParamT1, **kwargs
    ) -> Curry2[ParamT2, ParamT3, ReturnT, ArgKwargP]: ...
    @overload
    def __call__(
        self, arg1: ParamT1, arg2: ParamT2, **kwargs
    ) -> Curry1[ParamT3, ReturnT, ArgKwargP]: ...
    @overload
    def __call__(
        self, arg1: ParamT1, arg2: ParamT2, arg3: ParamT3, **kwargs
    ) -> ReturnT: ...
    def __call__(self, *args, **kwargs):
        return super().__call__(*args, **kwargs)


class Curry4(
    Curry[ParamT1, Curry3[ParamT2, ParamT3, ParamT4, ReturnT, ArgKwargP], ArgKwargP]
):
    def __call__(self, *args, **kwargs):
        return super().__call__(*args, **kwargs)


class Curry5(
    Curry[
        ParamT1,
        Curry4[ParamT2, ParamT3, ParamT4, ParamT5, ReturnT, ArgKwargP],
        ArgKwargP 
    ]
):
    def __call__(self, *args, **kwargs):
        return super().__call__(*args, **kwargs)


def curry(func, arity = None):
    return Curry(func=func, arity=arity)


def curry_right(func, arity = None):
    Curry(func=func, arity=arity, order=Order.RightToLeft)
