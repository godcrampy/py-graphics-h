from typing import List, Dict

from src.token.assignment import Assignment, AssignmentOperator
from src.token.binary_operation import BinaryOperation, BinaryOperator
from src.token.declaration import Declaration
from src.token.function_call import FunctionCall
from src.token.identifier import Identifier
from src.token.literal import Literal
from src.token.token import Token, LiteralType
# Delay execution
from src.token.unary_operation import UnaryOperation, UnaryOperator


def str_to_cast(value, type_str):
    if type_str == "int":
        return int(value) if value else int()
    if type_str == "string" or type_str == "char":
        res = str(value) if value else str()
        return res.strip("\"")
    return value


str_to_type: Dict[str, LiteralType] = {
    "int": LiteralType.INT,
    "string": LiteralType.STR,
    # TODO: Add char support if required
    "char": LiteralType.STR,
    "list": LiteralType.LIST
}


def generate_tokens(ast):
    tokens: List[Token] = []
    # find main
    nodes = get_main_nodes(ast)
    # generate token in main

    for node in nodes:
        token = tokenize_node(node)
        tokens.append(token)
    return tokens


def tokenize_node(node):
    node_type = node["_nodetype"]
    if node_type == "Decl":
        return handle_declaration(node)
    if node_type == "FuncCall":
        return handle_function_call(node)
    if node_type == "Assignment":
        return handle_assignment(node)
    if node_type == "ID":
        # RHS value is in variables
        return handle_id(node)
    if node_type == "Constant":
        # RHS value is literal
        return handle_constant(node)
    if node_type == "InitList":
        exprs = node["exprs"]
        list_vals = []
        for expr in exprs:
            list_vals.append(tokenize_node(expr))
        return Literal(list_vals, LiteralType.LIST)
    if node_type == "UnaryOp":
        op = node["op"]
        return UnaryOperation(tokenize_node(node["expr"]), UnaryOperator(op))
    if node_type == "BinaryOp":
        op = node["op"]
        return BinaryOperation(tokenize_node(node["left"]), tokenize_node(node["right"]), BinaryOperator(op))
    if node_type == "Return":
        return Literal(0, LiteralType.INT)
    raise Exception(f"Could not tokenize {node}")


def handle_assignment(node):
    op = node["op"]
    lvalue = node["lvalue"]
    rvalue = node["rvalue"]
    return Assignment(tokenize_node(lvalue), tokenize_node(rvalue), AssignmentOperator(op))


def handle_function_call(node):
    name = node["name"]["name"]
    args = node["args"]["exprs"] if node["args"] is not None else []
    params = []
    for arg in args:
        param = tokenize_node(arg)
        params.append(param)
    return FunctionCall(name, params)


def handle_declaration(node):
    # returns declaration variable
    init = node["init"]
    name = node["name"]
    identifier_type = get_identifier_type(node)
    if init is None:
        # no RHS value
        return Declaration(name, str_to_type[identifier_type], handle_empty_declaration(node))
    return Declaration(name, str_to_type[identifier_type], tokenize_node(init))


def handle_constant(node):
    identifier_type = node["type"]
    return Literal(str_to_cast(node["value"], identifier_type),
                   str_to_type[identifier_type])


def handle_id(node):
    name = node["name"]
    return Identifier(name, 0, LiteralType.VOID)


def handle_empty_declaration(node):
    identifier_type = get_identifier_type(node)
    return Literal(str_to_cast(None, identifier_type), str_to_type[identifier_type])


def get_main_nodes(ast):
    main_node = ast["ext"][0]
    main_node_items = main_node["body"]["block_items"]
    return main_node_items


def get_identifier_type(node):
    if node is None or "_nodetype" not in node:
        raise RuntimeError("Cannot find identifier_type of node")
    # FIXME: Feels Hacky
    if node["_nodetype"] == "ArrayDecl":
        type = get_identifier_type(node["type"])
        if type == "char":
            return "string"
        return "list"
    if node["_nodetype"] == "IdentifierType":
        return node["names"][0]
    return get_identifier_type(node["type"])
