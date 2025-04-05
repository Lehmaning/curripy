from functools import partial as partial_

from curripy import (
    add,
    cdot,
    compose,
    cond,
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
from curripy.dummies.func import return_0, return_1, return_false, return_true
from curripy.utils.cond import if_then
from curripy.utils.partial import partial_right


def test_curry():
    expr = (1 + 2) * 3
    assert curry(lambda x, y, z: (x + y) * z)(1)(2)(3) == expr
    assert curry_right(lambda x, y, z: (x + y) * z)(3)(2)(1) == expr


def test_curry_varargs():
    def __test_varargs(x, *args, **kwargs):
        return (
            x,
            *args,
        )

    assert curry(__test_varargs, arity=2)("a")(1, 2, 3) == ("a", 1, 2, 3)


def test_partial():
    assert partial(lambda x, y: 1, 1)(2) == partial_(lambda x, y: 1, 1)(2)
    assert partial(lambda x, y: 1, 1, 2)() == partial_(lambda x, y: 1, 1, 2)()


def test_partial_right():
    assert partial_right(lambda x, y: 1, 2)(1) == partial_(lambda x, y: 1, 1)(2)
    assert partial_right(lambda x, y: 1, 1, 2)() == partial_(lambda x, y: 1, 1, 2)()


def test_compose():
    expr = (3 + 1) * 2
    assert cdot(add(1))(mul(2))(3) == expr
    assert (
        dot(
            add(1),
            mul(2),
        )(3)
        == expr
    )
    assert (
        compose(
            mul(2),
            add(1),
        )(3)
        == expr
    )
    assert (
        pipe(
            add(1),
            mul(2),
        )(3)
        == expr
    )


def test_cond():
    def expr(x):
        return 1 if x == 2 else 0

    cond_single = if_then_else(eq(2))(return_1)(return_0)
    cond_spec = cond(
        if_(eq(2)),
        then(return_1),
        else_(return_0),
    )
    assert cond_single(1 + 1) == expr(1 + 1)
    assert cond_spec(1 + 1) == expr(1 + 1)
    assert cond_spec(1 + 2) == expr(1 + 2)


def test_if_then():
    assert if_then(lambda x: True)(return_true)("1") is True
    assert if_then(lambda x: False)(return_true)(1) == 1


def test_arity():
    assert curry(lambda x: 1)(1) == curry(lambda x: 1, arity=1)(1)
