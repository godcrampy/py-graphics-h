from typing import List, Dict

from pycparser import CParser

from src.generate_tokens import handle_declaration, get_main_nodes, handle_assignment
from src.parse_file import to_dict
from src.token.assignment import Assignment
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


def add_assignment_token(test_str):
    ast = parser.parse(test_str)
    nodes = get_main_nodes(to_dict(ast))
    assignment = handle_assignment(nodes[0], variables)
    tokens.append(assignment)
    variables[assignment.name] = assignment


add_token("int a = 5;")
add_token("int b = 10;")
add_token("char* c = \"Hello\";")
add_token("char* d = \"World\";")


def test_direct_integer_assignment():
    test_str = "int main(){a = 7;}"
    add_assignment_token(test_str)

    token = tokens[-1]
    assert token.token_type == TokenType.IDENTIFIER
    assert isinstance(token, Assignment)
    assert token.value == 7
    assert token.literal_type == LiteralType.INT
    assert token.name == "a"


def test_identifier_integer_assignment():
    test_str = "int main(){a = b;}"
    add_assignment_token(test_str)

    token = tokens[-1]
    assert token.token_type == TokenType.IDENTIFIER
    assert isinstance(token, Assignment)
    assert token.value == 10
    assert token.literal_type == LiteralType.INT
    assert token.name == "a"


def test_direct_integer_increment():
    test_str = "int main(){a += 7;}"
    add_assignment_token(test_str)

    token = tokens[-1]
    assert token.token_type == TokenType.IDENTIFIER
    assert isinstance(token, Assignment)
    assert token.value == 17
    assert token.literal_type == LiteralType.INT
    assert token.name == "a"


def test_identifier_integer_increment():
    test_str = "int main(){a += b;}"
    add_assignment_token(test_str)

    token = tokens[-1]
    assert token.token_type == TokenType.IDENTIFIER
    assert isinstance(token, Assignment)
    assert token.value == 27
    assert token.literal_type == LiteralType.INT
    assert token.name == "a"


def test_direct_string_assignment():
    test_str = "int main(){c = \"foo\";}"
    add_assignment_token(test_str)

    token = tokens[-1]
    assert token.token_type == TokenType.IDENTIFIER
    assert isinstance(token, Assignment)
    assert token.value == "foo"
    assert token.literal_type == LiteralType.STR
    assert token.name == "c"


def test_identifier_string_assignment():
    test_str = "int main(){c = d;}"
    add_assignment_token(test_str)

    token = tokens[-1]
    assert token.token_type == TokenType.IDENTIFIER
    assert isinstance(token, Assignment)
    assert token.value == "World"
    assert token.literal_type == LiteralType.STR
    assert token.name == "c"
