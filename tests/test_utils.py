from functools import partial as partial_

from curripy import (
    add,
    cdot,
    compose,
    curry,
    curry_right,
    dot,
    else_,
    eq,
    if_,
    if_then_else,
    mul,
    partial,
    pipe,
    then,
)
from curripy.dummies.func import return_1, return_0


def __test_varargs(x, *args, **kwargs):
    return x


def test_curry():
    assert curry(lambda x, y, z: (x + y) * z)(1)(2)(3) == (1 + 2) * 3
    assert curry_right(lambda x, y, z: (x + y) * z)(3)(2)(1) == (1 + 2) * 3
    assert curry(__test_varargs, arity=2)("a")(1, 2, 3) == "a"


def test_partial():
    assert partial(lambda x, y: 1, 1)(2) == partial_(lambda x, y: 1, 1)(2)
    assert partial(lambda x, y: 1, 1, 2)() == partial_(lambda x, y: 1, 1, 2)()


def test_compose():
    assert dot(add(1), mul(2))(3) == (3 + 1) * 2
    assert cdot(add(1))(mul(2))(3) == (3 + 1) * 2
    assert compose(mul(2), add(1))(3) == (3 + 1) * 2
    assert pipe(add(1), mul(2))(3) == (3 + 1) * 2


def test_cond():
    cond_flow = pipe(
        if_(eq(2)),
        then(return_1),
        else_(return_0),
    )

    cond_single = if_then_else(eq(2))(lambda x: 1)(lambda x: 0)

    assert cond_single(1 + 1) == (1 if 1 + 1 == 2 else 0)
    assert cond_flow(1 + 1) == (1 if 1 + 1 == 2 else 0)
