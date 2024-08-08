from functools import partial as partial_

from curripy import (
    add,
    cdot,
    compose,
    curry,
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


def test_curry():
    assert curry(lambda x, y, z: x + y + z)(1)(2)(3) == 1 + 2 + 3


def test_partial():
    assert not isinstance(partial(lambda x, y: 1, 1, y=2), partial_)
    assert partial(lambda x, y: 1, 1, y=2)() == partial_(lambda x, y: 1, 1)(2)


def test_compose():
    assert dot(add(1), mul(2))(3) == (3 + 1) * 2
    assert cdot(add(1))(mul(2))(3) == (3 + 1) * 2
    assert compose(mul(2), add(1))(3) == (3 + 1) * 2
    assert pipe(add(1), mul(2))(3) == (3 + 1) * 2


def test_cond():
    cond_flow = pipe(
        if_(eq(2)),
        then(lambda x: 1),
        else_(lambda x: 0),
    )

    cond_single = if_then_else(eq(2))(lambda x: 1)(lambda x: 0)

    assert cond_single(1 + 1) == 1 if 1 + 1 == 2 else 0
    assert cond_flow(1 + 1) == 1 if 1 + 1 == 2 else 0
