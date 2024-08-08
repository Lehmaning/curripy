from curripy import eq, filter_, isinstance_, map_, pipe


def test_isinstance():
    assert isinstance_(str)("a") == isinstance("a", str)


def test_filter():
    assert tuple(filter_(None)([None])) == tuple(filter(None, [None]))


def test_map():
    point_free_pipe = pipe(map_(eq(2)), tuple)
    evaluated_map = tuple(map(lambda x: x == 2, [1, 2, 3]))
    assert point_free_pipe([1, 2, 3]) == (
        False,
        True,
        False,
    )
    assert point_free_pipe([1, 2, 3]) == evaluated_map
