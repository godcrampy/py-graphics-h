from typing import List, Dict

from src.token.assignment import Assignment
from src.token.function_call import FunctionCall
from src.token.identifier import Identifier
from src.token.literal import Literal
from src.token.token import Token, LiteralType


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
    "char": LiteralType.STR
}


def generate_tokens(ast, variables: Dict[str, Identifier]):
    tokens: List[Token] = []
    # find main
    nodes = get_main_nodes(ast)
    # generate token in main

    for node in nodes:
        node_type = node["_nodetype"]
        if node_type == "Decl":
            identifier = handle_declaration(node, variables)
            tokens.append(identifier)
            variables[identifier.name] = identifier
        elif node_type == "FuncCall":
            function = handle_function_call(node, variables)
            tokens.append(function)
        elif node_type == "Assignment":
            assignment = handle_assignment(node, variables)
            variables[assignment.name] = Identifier(assignment.name, assignment.value, assignment.literal_type)
            tokens.append(assignment)
    return tokens


def handle_assignment(node, variables):
    op = node["op"]
    lvalue = node["lvalue"]
    rvalue = node["rvalue"]
    rtype = rvalue["_nodetype"]
    literal = Literal(0, LiteralType.INT)
    if rtype == "Constant":
        literal = Literal(str_to_cast(rvalue["value"], rvalue["type"]),
                          str_to_type[rvalue["type"]])
    elif rtype == "ID":
        identifier = variables[rvalue["name"]]
        literal = Literal(identifier.value, identifier.literal_type)
    identifier: Identifier = variables[lvalue["name"]]
    assignment = Assignment(identifier.name, identifier.value, identifier.literal_type)
    if op == "=":
        assignment = Assignment(identifier.name, literal.value, literal.literal_type)
    elif op == "+=":
        assignment = Assignment(identifier.name, identifier.value + literal.value, literal.literal_type)
    return assignment


def handle_function_call(node, variables):
    name = node["name"]["name"]
    args = node["args"]["exprs"] if node["args"] is not None else []
    params = []
    for arg in args:
        literal = handle_argument(arg, node, variables)
        params.append(literal)
    return FunctionCall(name, params)


def handle_argument(arg, node, variables):
    node_type = arg["_nodetype"]
    if node_type == "Constant":
        return handle_constant_argument(arg)
    if node_type == "ID":
        return handle_identifier_argument(arg, variables)
    if node_type == "UnaryOp":
        op = arg["op"]
        if op == "&":
            return handle_identifier_argument(arg["expr"], variables)
        if op == "-":
            literal = handle_argument(arg["expr"], node, variables)
            literal.value *= -1
            return literal
        raise Exception(f"Unexpected unaryOp {op} for parameter: {node['coord']}")
    if node_type == "BinaryOp":
        left = handle_argument(arg["left"], node, variables)
        right = handle_argument(arg["right"], node, variables)
        op = arg["op"]
        if op == "+":
            return Literal(left.value + right.value, left.literal_type)
        if op == "-":
            return Literal(left.value - right.value, left.literal_type)
        if op == "*":
            return Literal(left.value * right.value, left.literal_type)
        if op == "/":
            return Literal(left.value / right.value, left.literal_type)

    raise Exception(f"Unexpected node_type for parameter: {node['coord']}")


def handle_identifier_argument(arg, variables):
    identifier = variables[arg["name"]]
    literal = Literal(identifier.value, identifier.literal_type)
    return literal


def handle_constant_argument(arg):
    literal = Literal(str_to_cast(arg["value"], arg["type"]), str_to_type[arg["type"]])
    return literal


def handle_declaration(node, variables):
    # new identifier (variable) is created
    init = node["init"]
    if init is None:
        # no RHS value
        return handle_empty_declaration(node)
    declaration_type = init["_nodetype"]
    if declaration_type == "ID":
        # RHS value is in variables
        return handle_identifier_declaration(node, variables)
    if declaration_type == "Constant":
        # RHS value is literal
        return handle_literal_declaration(node)
    if declaration_type == "InitList":
        exprs = init["exprs"]
        list_vals = []
        for expr in exprs:
            if expr["_nodetype"] == "Constant":
                list_vals.append(str_to_cast(expr["value"], expr["type"]))
            elif expr["_nodetype"] == "ID":
                identifier = variables[expr["name"]]
                list_vals.append(identifier.value)
        return Identifier(node["name"], list_vals, LiteralType.LIST)
    raise Exception(f"Unexpected RHS of variable: {declaration_type} {node['coord']}")


def handle_literal_declaration(node):
    identifier_type = get_identifier_type(node)
    init = node["init"]
    name = node["name"]
    return Identifier(name, str_to_cast(init["value"], identifier_type),
                      str_to_type[identifier_type])


def handle_identifier_declaration(node, variables):
    init = node["init"]
    name = node["name"]
    referenced_identifier = variables[init["name"]]
    return Identifier(name, referenced_identifier.value, referenced_identifier.literal_type)


def handle_empty_declaration(node):
    identifier_type = get_identifier_type(node)
    name = node["name"]
    return Identifier(name, str_to_cast(None, identifier_type), str_to_type[identifier_type])


def get_main_nodes(ast):
    main_node = ast["ext"][0]
    main_node_items = main_node["body"]["block_items"]
    return main_node_items


def get_identifier_type(node):
    if node is None or "_nodetype" not in node:
        raise RuntimeError("Cannot find identifier_type of node")
    if node["_nodetype"] == "IdentifierType":
        return node["names"][0]
    return get_identifier_type(node["type"])
