from src.token.token import Token
from test.util import add_token, wrap_with_main


def test_return():
    test_str = wrap_with_main("int a = 5;return a;")
    tokens = add_token(test_str)

    token = tokens[-1]
    assert isinstance(token, Token)
    assert token.eval({'a': 5}) == 5
