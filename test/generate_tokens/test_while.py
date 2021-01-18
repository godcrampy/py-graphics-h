from src.token.while_flow import WhileFlow
from test.util import add_token, wrap_with_main


def test_while():
    test_str = wrap_with_main("while(a < 5) {a += 1;}")
    tokens = add_token(test_str)

    token = tokens[-1]
    assert isinstance(token, WhileFlow)
    variables = {'a': 0}
    token.eval(variables)
    assert variables["a"] == 5
