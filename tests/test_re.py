from curripy.re_ import search
import re

def test_search():
    assert search("a")("a") is not None