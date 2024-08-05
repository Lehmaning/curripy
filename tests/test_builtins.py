from curripy.utils import pipe
from curripy import else_, if_, if_then_else, then, map_, filter_, isinstance_
from curripy.operator_ import eq


def test_isinstance():
    assert isinstance_(str)("a") == isinstance("a", str)


def test_filter():
    assert filter_(None)([None]) == filter(None, [None])


def test_map():
    point_free_pipe = pipe(map_(eq(2)), tuple)
    evaluated_map = tuple(map_(eq(2))([1, 2, 3]))
    assert point_free_pipe([1, 2, 3]) == (
        False,
        True,
        False,
    ) and evaluated_map == (
        False,
        True,
        False,
    )


def test_if_then_else():
    cond_flow = pipe(
        if_(eq(2)),
        then_(lambda x: 1),
        else_(lambda x: 0),
    )

    cond_single = if_then_else(
        eq(2),
        lambda x: 1,
        lambda x: 0,
    )

    assert cond_flow(1 + 1) == 1 and cond_single(1 + 1) == 1
