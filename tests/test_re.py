from curripy.re_ import search


def test_search():
    assert search("a")("b") is None
    assert search("a")("a") is not None
