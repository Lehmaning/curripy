from curripy import eq, filter_, isinstance_, map_


def test_isinstance():
    is_str = isinstance_(str)
    assert is_str("a") == isinstance("a", str)


def test_filter():
    filter_none = filter_(None)
    assert tuple(filter_none([None])) == tuple(filter(None, [None]))


def test_map():
    all_eq_2 = map_(eq(2))
    evaluated_map = tuple(map(lambda x: x == 2, [1, 2, 3]))
    assert tuple(all_eq_2([1, 2, 3])) == (
        False,
        True,
        False,
    )
    assert tuple(all_eq_2([1, 2, 3])) == evaluated_map
