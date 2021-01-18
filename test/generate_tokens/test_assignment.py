from src.token.assignment import Assignment, AssignmentOperator
from src.token.binary_operation import BinaryOperation
from src.token.identifier import Identifier
from src.token.literal import Literal
from test.util import wrap_with_main, add_token


def test_direct_integer_assignment():
    test_str = wrap_with_main("a = 7;")
    tokens = add_token(test_str)

    token = tokens[-1]
    assert isinstance(token, Assignment)
    assert token.operator == AssignmentOperator("=")
    assert isinstance(token.left, Identifier)
    assert isinstance(token.right, Literal)

    assert token.left.name == "a"
    assert token.right.value == 7


def test_identifier_integer_assignment():
    test_str = wrap_with_main("a = b + 7;")
    tokens = add_token(test_str)

    token = tokens[-1]
    assert isinstance(token, Assignment)
    assert token.operator == AssignmentOperator("=")
    assert isinstance(token.left, Identifier)
    assert isinstance(token.right, BinaryOperation)
    assert isinstance(token.right.left, Identifier)
    assert isinstance(token.right.right, Literal)

    assert token.right.left.name == "b"
    assert token.right.right.value == 7


def test_direct_integer_increment():
    test_str = wrap_with_main("a += c + 7;")
    tokens = add_token(test_str)

    token = tokens[-1]
    assert isinstance(token, Assignment)
    assert token.operator == AssignmentOperator("+=")
    assert isinstance(token.left, Identifier)
    assert isinstance(token.right, BinaryOperation)
    assert isinstance(token.right.left, Identifier)
    assert isinstance(token.right.right, Literal)

    assert token.right.left.name == "c"
    assert token.right.right.value == 7


def test_direct_string_assignment():
    test_str = wrap_with_main("d = \"foo\";")
    tokens = add_token(test_str)

    token = tokens[-1]
    assert isinstance(token, Assignment)
    assert token.operator == AssignmentOperator("=")
    assert isinstance(token.left, Identifier)
    assert isinstance(token.right, Literal)

    assert token.left.name == "d"
    assert token.right.value == "foo"


def test_identifier_string_assignment():
    test_str = wrap_with_main("d = g;")
    tokens = add_token(test_str)

    token = tokens[-1]
    assert isinstance(token, Assignment)
    assert token.operator == AssignmentOperator("=")
    assert isinstance(token.left, Identifier)
    assert isinstance(token.right, Identifier)

    assert token.left.name == "d"
    assert token.right.name == "g"


def test_assignement_eval():
    test_str = wrap_with_main("{a += g;b -= g;c /= g; d *= g;}")
    tokens = add_token(test_str)

    token = tokens[-1]
    variables = {'a': 5, 'b': 4, 'c': 14, 'd': 10, 'g': 2}
    token.eval(variables)
    assert variables['a'] == 7
    assert variables['b'] == 2
    assert variables['c'] == 7
    assert variables['d'] == 20
    assert variables['g'] == 2
