from src.token.compound import Compound
from test.util import wrap_with_main, add_token


def test_arithmetic_operations():
    test_str = wrap_with_main("{int z = 10; a = 1 + z; b = z / 2; c = z - 2; d = z * 2;}")
    tokens = add_token(test_str)

    token = tokens[-1]
    assert isinstance(token, Compound)
    variables = {}
    token.eval(variables)
    assert variables['z'] == 10
    assert variables['a'] == 11
    assert variables['b'] == 5
    assert variables['c'] == 8
    assert variables['d'] == 20


def test_logical_operations():
    test_str = wrap_with_main("{a = 1 == z; b = z < 2; c = z > 2; d = z >= 2; e = z <= 2; f = z != 2;}")
    tokens = add_token(test_str)

    token = tokens[-1]
    assert isinstance(token, Compound)
    variables = {'z': 10}
    token.eval(variables)
    assert not variables['a']
    assert not variables['b']
    assert variables['c']
    assert variables['d']
    assert not variables['e']
    assert variables['f']
