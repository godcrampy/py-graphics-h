from src.token.if_flow import IfFlow
from src.token.while_flow import WhileFlow
from test.util import add_token, wrap_with_main


def test_if():
    test_str = wrap_with_main("if(a < b) {a = 100;} else if(a == b) {b = 100;} else {b = 1000;}")
    tokens = add_token(test_str)

    token = tokens[-1]
    assert isinstance(token, IfFlow)
    variables = {'a': 0, 'b': 8}
    token.eval(variables)
    assert variables["a"] == 100
    assert variables["b"] == 8
