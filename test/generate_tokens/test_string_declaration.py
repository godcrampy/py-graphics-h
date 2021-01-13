from typing import List, Dict

from pycparser import CParser

from src.generate_tokens import handle_declaration
from src.parse_file import to_dict
from src.token.identifier import Identifier
from src.token.token import Token, TokenType, LiteralType

parser = CParser()
tokens: List[Token] = []
variables: Dict[str, Identifier] = {}


def add_token(test_str):
    ast = parser.parse(test_str)
    node = to_dict(ast)["ext"][0]
    handle_declaration(node, tokens, variables)


def test_direct_string_array_declaration():
    test_str = "char d[] = \"Hello\";"
    add_token(test_str)

    token = tokens[-1]
    assert token.token_type == TokenType.IDENTIFIER
    assert isinstance(token, Identifier)
    assert token.value == "Hello"
    assert token.literal_type == LiteralType.STR
    assert token.name == "d"
    assert "d" in variables
    assert variables["d"] == token


def test_direct_string_pointer_declaration():
    test_str = "char* e = \"World\";"
    add_token(test_str)

    token = tokens[-1]
    assert token.token_type == TokenType.IDENTIFIER
    assert isinstance(token, Identifier)
    assert token.value == "World"
    assert token.literal_type == LiteralType.STR
    assert token.name == "e"
    assert "e" in variables
    assert variables["e"] == token


def test_assigned_string_array_declaration():
    test_str = "char f[] = d;"
    add_token(test_str)

    token = tokens[-1]
    assert token.token_type == TokenType.IDENTIFIER
    assert isinstance(token, Identifier)
    assert token.value == "Hello"
    assert token.literal_type == LiteralType.STR
    assert token.name == "f"
    assert "f" in variables
    assert variables["f"] == token


def test_assigned_string_pointer_declaration():
    test_str = "char* g = e;"
    add_token(test_str)

    token = tokens[-1]
    assert token.token_type == TokenType.IDENTIFIER
    assert isinstance(token, Identifier)
    assert token.value == "World"
    assert token.literal_type == LiteralType.STR
    assert token.name == "g"
    assert "g" in variables
    assert variables["g"] == token


def test_uninitialised_string_array_declaration():
    test_str = "char h[];"
    add_token(test_str)

    token = tokens[-1]
    assert token.token_type == TokenType.IDENTIFIER
    assert isinstance(token, Identifier)
    assert token.value == ""
    assert token.literal_type == LiteralType.STR
    assert token.name == "h"
    assert "h" in variables
    assert variables["h"] == token


def test_uninitialised_string_pointer_declaration():
    test_str = "char* i;"
    add_token(test_str)

    token = tokens[-1]
    assert token.token_type == TokenType.IDENTIFIER
    assert isinstance(token, Identifier)
    assert token.value == ""
    assert token.literal_type == LiteralType.STR
    assert token.name == "i"
    assert "i" in variables
    assert variables["i"] == token
