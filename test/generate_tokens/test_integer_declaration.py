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
    identifier = handle_declaration(node, variables)
    tokens.append(identifier)
    variables[identifier.name] = identifier


def test_direct_integer_declaration():
    test_str = "int a = 5;"
    add_token(test_str)

    token = tokens[-1]
    assert token.token_type == TokenType.IDENTIFIER
    assert isinstance(token, Identifier)
    assert token.value == 5
    assert token.literal_type == LiteralType.INT
    assert token.name == "a"
    assert "a" in variables
    assert variables["a"] == token


def test_assigned_integer_declaration():
    test_str = "int b = a;"
    add_token(test_str)

    token = tokens[-1]
    assert token.token_type == TokenType.IDENTIFIER
    assert isinstance(token, Identifier)
    assert token.value == 5
    assert token.literal_type == LiteralType.INT
    assert token.name == "b"
    assert "b" in variables
    assert variables["b"] == token


def test_uninitialised_integer_declaration():
    test_str = "int c;"
    add_token(test_str)

    token = tokens[-1]
    assert token.token_type == TokenType.IDENTIFIER
    assert isinstance(token, Identifier)
    assert token.value == 0
    assert token.literal_type == LiteralType.INT
    assert token.name == "c"
    assert "c" in variables
    assert variables["c"] == token


def test_list_declaration():
    test_str = "int d[5] = {1, 2, 3, 4, 5, c};"
    add_token(test_str)

    token = tokens[-1]
    assert token.token_type == TokenType.IDENTIFIER
    assert isinstance(token, Identifier)
    assert token.value == [1, 2, 3, 4, 5, 0]
    assert token.literal_type == LiteralType.LIST
    assert token.name == "d"
    assert "d" in variables
    assert variables["d"] == token
