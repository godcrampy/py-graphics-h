from src.token.compound import Compound
from test.util import wrap_with_main, add_token


def test_amp_operation():
    test_str = wrap_with_main("{int z = 1; int a = &z;}")
    tokens = add_token(test_str)

    token = tokens[-1]
    assert isinstance(token, Compound)
    variables = {}
    token.eval(variables)
    assert variables['z'] == 1
    assert variables['a'] == 1


def test_minus_operation():
    test_str = wrap_with_main("{int z = 1; int a = -z;}")
    tokens = add_token(test_str)

    token = tokens[-1]
    assert isinstance(token, Compound)
    variables = {}
    token.eval(variables)
    assert variables['z'] == 1
    assert variables['a'] == -1


def test_increment_operation():
    test_str = wrap_with_main("{int z = 1; int a = z++; int b = ++z;}")
    tokens = add_token(test_str)

    token = tokens[-1]
    assert isinstance(token, Compound)
    variables = {}
    token.eval(variables)
    assert variables['z'] == 3
    assert variables['a'] == 1
    assert variables['b'] == 3


def test_decrement_operation():
    test_str = wrap_with_main("{int z = 1; int a = z--; int b = --z;}")
    tokens = add_token(test_str)

    token = tokens[-1]
    assert isinstance(token, Compound)
    variables = {}
    token.eval(variables)
    assert variables['z'] == -1
    assert variables['a'] == 1
    assert variables['b'] == -1
