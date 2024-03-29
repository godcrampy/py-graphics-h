from src.generate_tokens import generate_tokens
from src.parse_file import get_ast
from src.token.assignment import Assignment
from src.token.declaration import Declaration
from src.token.function_call import FunctionCall
from src.token.identifier import Identifier
from src.token.literal import Literal
from src.token.token import LiteralType


def test_generate_token():
    ast = get_ast("test/generate_tokens/main.c")
    variables = {}
    tokens = generate_tokens(ast)
    assert isinstance(tokens, list)
    assert len(tokens) == 3
    assert isinstance(tokens[0], Declaration)
    assert tokens[0].name == "msg"

    assert isinstance(tokens[1], FunctionCall)
    assert tokens[1].name == "printf"
    params = tokens[1].params
    assert isinstance(params, list)
    assert len(params) == 2
    arg1 = params[0]
    arg2 = params[1]
    assert isinstance(arg1, Literal)
    assert arg1.value == "%s\\n"
    assert arg1.literal_type == LiteralType.STR
    assert isinstance(arg2, Identifier)
    assert arg2.name == "msg"

    assert isinstance(tokens[2], Assignment)
    assert tokens[2].left.name == "msg"
    assert tokens[2].right.value == "Hello"
