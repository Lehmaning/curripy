"""
Generic types which are signed for types of return values and types of parameters.
Splitting them into a module for reusing.
"""

from typing import TypeVar, ParamSpec

__all__ = [
    "ReturnT",
    "ReturnT1",
    "ReturnT2",
    "ReturnT3",
    "ReturnT4",
    "ReturnT5",
    "ParamT",
    "ParamT1",
    "ParamT2",
    "ParamT3",
    "ParamT4",
    "ParamT5",
    "ArgKwargP",
]

ReturnT = TypeVar("ReturnT")
ReturnT1 = TypeVar("ReturnT1")
ReturnT2 = TypeVar("ReturnT2")
ReturnT3 = TypeVar("ReturnT3")
ReturnT4 = TypeVar("ReturnT4")
ReturnT5 = TypeVar("ReturnT5")

ParamT = TypeVar("ParamT")
ParamT1 = TypeVar("ParamT1")
ParamT2 = TypeVar("ParamT2")
ParamT3 = TypeVar("ParamT3")
ParamT4 = TypeVar("ParamT4")
ParamT5 = TypeVar("ParamT5")

ArgKwargP = ParamSpec("ArgKwargP")
