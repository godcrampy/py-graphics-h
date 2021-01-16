from typing import List

from src.token.binary_operation import BinaryOperation, BinaryOperator
from src.token.function_call import FunctionCall
from src.token.identifier import Identifier
from src.token.literal import Literal
from src.token.token import LiteralType
from src.token.unary_operation import UnaryOperator, UnaryOperation
from test.util import wrap_with_main, add_token


def test_empty_function():
    test_str = wrap_with_main("foo();")
    tokens = add_token(test_str)

    token = tokens[-1]
    assert isinstance(token, FunctionCall)
    assert token.name == "foo"
    assert isinstance(token.params, List)
    assert len(token.params) == 0


def test_args():
    test_str = wrap_with_main("bar(123, b, a, \"world\");")
    tokens = add_token(test_str)

    token = tokens[-1]
    assert isinstance(token, FunctionCall)
    assert token.name == "bar"
    assert isinstance(token.params, List)
    assert len(token.params) == 4
    params: List = token.params
    assert isinstance(params[0], Literal)
    assert isinstance(params[1], Identifier)
    assert isinstance(params[2], Identifier)
    assert isinstance(params[3], Literal)

    assert params[0].value == 123
    assert params[0].literal_type == LiteralType.INT

    assert params[1].name == "b"

    assert params[2].name == "a"

    assert params[3].value == "world"
    assert params[3].literal_type == LiteralType.STR


def test_unary():
    test_str = wrap_with_main("baz(&b, -a);")
    tokens = add_token(test_str, True)

    token = tokens[-1]
    assert isinstance(token, FunctionCall)
    assert token.name == "baz"
    assert isinstance(token.params, List)
    assert len(token.params) == 2
    params: List = token.params
    assert isinstance(params[0], UnaryOperation)
    assert isinstance(params[1], UnaryOperation)

    assert params[0].operator == UnaryOperator("&")
    assert isinstance(params[0].token, Identifier)
    assert params[0].token.name == "b"

    assert params[1].operator == UnaryOperator("-")
    assert isinstance(params[1].token, Identifier)
    assert params[1].token.name == "a"


def test_binary_operation():
    test_str = wrap_with_main("qux(a + a, 6 - 5, a * 5, 15 / a);")
    tokens = add_token(test_str, True)

    token = tokens[-1]
    assert isinstance(token, FunctionCall)
    assert token.name == "qux"
    assert isinstance(token.params, List)
    assert len(token.params) == 4
    params: List = token.params
    assert isinstance(params[0], BinaryOperation)
    assert isinstance(params[1], BinaryOperation)
    assert isinstance(params[2], BinaryOperation)
    assert isinstance(params[3], BinaryOperation)

    assert params[0].operator == BinaryOperator("+")
    assert isinstance(params[0].left, Identifier)
    assert isinstance(params[0].right, Identifier)
    assert params[0].left.name == "a"
    assert params[0].right.name == "a"

    assert params[1].operator == BinaryOperator("-")
    assert isinstance(params[1].left, Literal)
    assert isinstance(params[1].right, Literal)
    assert params[1].left.value == 6
    assert params[1].right.value == 5

    assert params[2].operator == BinaryOperator("*")
    assert isinstance(params[2].left, Identifier)
    assert isinstance(params[2].right, Literal)
    assert params[2].left.name == "a"
    assert params[2].right.value == 5

    assert params[3].operator == BinaryOperator("/")
    assert isinstance(params[3].left, Literal)
    assert isinstance(params[3].right, Identifier)
    assert params[3].left.value == 15
    assert params[3].right.name == "a"
