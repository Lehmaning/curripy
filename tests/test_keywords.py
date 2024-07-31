from curripy.modules.operator_ import eq
from curripy.functionalize_tools import pipe
from curripy.pointfree.keywords import else_, if_, if_then_else, then_



def test_cond():
    cond_flow = pipe(
        if_(eq(2)),
        then_(lambda x: 1),
        else_(lambda x: 0),
    )(1 + 1)
    
    cond_single = if_then_else(
        eq(2),
        lambda x: 1,
        lambda x: 0,
    )(1 + 1)
    
    assert cond_flow == cond_single
