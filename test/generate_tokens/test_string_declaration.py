from src.token.declaration import Declaration
from src.token.identifier import Identifier
from src.token.literal import Literal
from src.token.token import LiteralType
from test.util import add_token, wrap_with_main


def test_direct_string_array_declaration():
    test_str = wrap_with_main("char d[] = \"Hello\";")
    tokens = add_token(test_str)

    token = tokens[-1]
    assert isinstance(token, Declaration)
    assert token.name == "d"
    assert token.literal_type == LiteralType.STR
    rhs = token.right
    assert isinstance(rhs, Literal)
    assert rhs.literal_type == LiteralType.STR
    assert rhs.value == "Hello"


def test_direct_string_pointer_declaration():
    test_str = wrap_with_main("char* e = \"World\";")
    tokens = add_token(test_str)

    token = tokens[-1]
    assert isinstance(token, Declaration)
    assert token.name == "e"
    assert token.literal_type == LiteralType.STR
    rhs = token.right
    assert isinstance(rhs, Literal)
    assert rhs.literal_type == LiteralType.STR
    assert rhs.value == "World"


def test_assigned_string_array_declaration():
    test_str = wrap_with_main("char f[] = d;")
    tokens = add_token(test_str)

    token = tokens[-1]
    assert isinstance(token, Declaration)
    assert token.name == "f"
    assert token.literal_type == LiteralType.STR
    rhs = token.right
    assert isinstance(rhs, Identifier)
    assert rhs.name == "d"


def test_assigned_string_pointer_declaration():
    test_str = wrap_with_main("char* g = e;")

    tokens = add_token(test_str)

    token = tokens[-1]
    assert isinstance(token, Declaration)
    assert token.name == "g"
    assert token.literal_type == LiteralType.STR
    rhs = token.right
    assert isinstance(rhs, Identifier)
    assert rhs.name == "e"


def test_uninitialised_string_array_declaration():
    test_str = wrap_with_main("char h[];")

    tokens = add_token(test_str)

    token = tokens[-1]
    assert isinstance(token, Declaration)
    assert token.name == "h"
    assert token.literal_type == LiteralType.STR
    rhs = token.right
    assert isinstance(rhs, Literal)
    assert rhs.literal_type == LiteralType.STR
    assert rhs.value == ""


def test_uninitialised_string_pointer_declaration():
    test_str = wrap_with_main("char* i;")
    tokens = add_token(test_str)

    token = tokens[-1]
    assert isinstance(token, Declaration)
    assert token.name == "i"
    assert token.literal_type == LiteralType.STR
    rhs = token.right
    assert isinstance(rhs, Literal)
    assert rhs.literal_type == LiteralType.STR
    assert rhs.value == ""
