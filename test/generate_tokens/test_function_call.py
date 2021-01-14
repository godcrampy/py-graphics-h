from typing import List, Dict

from pycparser import CParser

from src.generate_tokens import handle_function_call, get_main_nodes, handle_declaration
from src.parse_file import to_dict
from src.token.function_call import FunctionCall
from src.token.identifier import Identifier
from src.token.literal import Literal
from src.token.token import Token, LiteralType

parser = CParser()
tokens: List[Token] = []
variables: Dict[str, Identifier] = {}


def add_identifier_token(test_str):
    ast = parser.parse(test_str)
    node = to_dict(ast)["ext"][0]
    handle_declaration(node, tokens, variables)


def add_function_call_token(test_str):
    ast = parser.parse(test_str)
    nodes = get_main_nodes(to_dict(ast))
    handle_function_call(nodes[0], tokens, variables)


add_identifier_token("int a = 5;")
add_identifier_token("char* b = \"hello\";")


def test_empty_function():
    test_str = "int main() {foo();}"
    add_function_call_token(test_str)
    token = tokens[-1]
    assert isinstance(token, FunctionCall)
    assert token.name == "foo"
    assert isinstance(token.params, List)
    assert len(token.params) == 0


def test_args():
    test_str = "int main() {bar(123, b, a, \"world\");}"
    add_function_call_token(test_str)
    token = tokens[-1]
    assert isinstance(token, FunctionCall)
    assert token.name == "bar"
    assert isinstance(token.params, List)
    assert len(token.params) == 4
    params: List[Literal] = token.params
    assert isinstance(params[0], Literal)
    assert isinstance(params[1], Literal)
    assert isinstance(params[2], Literal)
    assert isinstance(params[3], Literal)

    assert params[0].value == 123
    assert params[0].literal_type == LiteralType.INT

    assert params[1].value == "hello"
    assert params[1].literal_type == LiteralType.STR

    assert params[2].value == 5
    assert params[2].literal_type == LiteralType.INT

    assert params[3].value == "world"
    assert params[3].literal_type == LiteralType.STR


def test_ampersand():
    test_str = "int main() {baz(&a, &b);}"
    add_function_call_token(test_str)
    token = tokens[-1]
    assert isinstance(token, FunctionCall)
    assert token.name == "baz"
    assert isinstance(token.params, List)
    assert len(token.params) == 2
    params: List[Literal] = token.params
    assert isinstance(params[0], Literal)
    assert isinstance(params[1], Literal)

    assert params[0].value == 5
    assert params[0].literal_type == LiteralType.INT

    assert params[1].value == "hello"
    assert params[1].literal_type == LiteralType.STR
