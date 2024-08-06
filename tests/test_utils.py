from curripy.utils import partial, curry
from functools import partial as partial_

def test_partial():
    assert not isinstance(partial(lambda x, y: 1, 1, y=2), partial_)
    assert partial(lambda x, y: 1, 1, y=2)() == partial_(lambda x, y: 1, 1)(2)
