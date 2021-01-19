from typing import List

from src.token.binary_operation import BinaryOperation, BinaryOperator
from src.token.declaration import Declaration
from src.token.identifier import Identifier
from src.token.literal import Literal
from src.token.token import LiteralType
from test.util import add_token, wrap_with_main


def test_direct_integer_declaration():
    test_str = wrap_with_main("int a = 5;")
    tokens = add_token(test_str)

    token = tokens[-1]
    assert isinstance(token, Declaration)
    assert token.name == "a"
    assert token.literal_type == LiteralType.INT
    rhs = token.right
    assert isinstance(rhs, Literal)
    assert rhs.literal_type == LiteralType.INT
    assert rhs.value == 5


def test_assigned_integer_declaration():
    test_str = wrap_with_main("int b = a;")
    tokens = add_token(test_str)

    token = tokens[-1]
    assert isinstance(token, Declaration)
    assert token.name == "b"
    assert token.literal_type == LiteralType.INT
    rhs = token.right
    assert isinstance(rhs, Identifier)
    assert rhs.name == "a"


def test_operation_integer_declaration():
    test_str = wrap_with_main("int b = a + 5;")
    tokens = add_token(test_str)

    token = tokens[-1]
    assert isinstance(token, Declaration)
    assert token.name == "b"
    assert token.literal_type == LiteralType.INT
    rhs = token.right
    assert isinstance(rhs, BinaryOperation)

    assert rhs.operator == BinaryOperator("+")
    assert isinstance(rhs.left, Identifier)
    assert isinstance(rhs.right, Literal)
    assert rhs.left.name == "a"
    assert rhs.right.value == 5


def test_uninitialised_integer_declaration():
    test_str = wrap_with_main("int c;")
    tokens = add_token(test_str)

    token = tokens[-1]

    assert isinstance(token, Declaration)
    assert token.name == "c"
    assert token.literal_type == LiteralType.INT
    rhs = token.right
    assert isinstance(rhs, Literal)
    assert rhs.literal_type == LiteralType.INT
    assert rhs.value == 0


def test_list_declaration():
    test_str = wrap_with_main("int d[5] = {1, c};")

    tokens = add_token(test_str)

    token = tokens[-1]
    assert isinstance(token, Declaration)
    assert token.name == "d"
    assert token.literal_type == LiteralType.LIST
    rhs = token.right
    assert isinstance(rhs, Literal)
    assert rhs.literal_type == LiteralType.LIST
    assert isinstance(rhs.value, List)
    assert len(rhs.value) == 2
    first = rhs.value[0]
    second = rhs.value[1]

    assert isinstance(first, Literal)
    assert first.value == 1
    assert first.literal_type == LiteralType.INT

    assert isinstance(second, Identifier)
    assert second.name == "c"
