from test.util import add_token, wrap_with_main


def test_for():
    test_str = wrap_with_main("for(int i = 0; i < 5; ++i) { ++a; }")
    tokens = add_token(test_str)

    token = tokens[-1]
    variables = {'a': 1}
    token.eval(variables)
    assert variables["a"] == 6
    assert variables["i"] == 5
