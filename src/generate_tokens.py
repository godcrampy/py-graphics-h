from typing import List, Dict

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
            handle_declaration(node, tokens, variables)
        elif node_type == "FuncCall":
            handle_function_call(node, tokens, variables)

    return tokens


def handle_function_call(node, tokens, variables):
    name = node["name"]["name"]
    args = node["args"]["exprs"] if node["args"] is not None else []
    params = []
    for arg in args:
        node_type = arg["_nodetype"]
        if node_type == "Constant":
            literal = Literal(str_to_cast(arg["value"], arg["type"]), str_to_type[arg["type"]])
            params.append(literal)
        elif node_type == "ID":
            identifier = variables[arg["name"]]
            literal = Literal(identifier.value, identifier.literal_type)
            params.append(literal)
        elif node_type == "UnaryOp":
            identifier = variables[arg["expr"]["name"]]
            literal = Literal(identifier.value, identifier.literal_type)
            params.append(literal)
        else:
            raise Exception(f"Unexpected node_type for parameter: {node['coord']}")
    function = FunctionCall(name, params)
    tokens.append(function)


def handle_declaration(node, tokens, variables):
    # new identifier (variable) is created
    name = node["name"]
    init = node["init"]
    identifier_type = get_identifier_type(node)
    if init is None:
        # no RHS value
        handle_empty_declaration(identifier_type, name, tokens, variables)
    else:
        declaration_type = init["_nodetype"]
        if declaration_type == "ID":
            # RHS value is in variables
            handle_identifier_declaration(init, name, tokens, variables)
        elif declaration_type == "Constant":
            # RHS value is literal
            handle_literal_declaration(identifier_type, init, name, tokens, variables)
        else:
            raise Exception(f"Unexpected RHS of variable: {node['coord']}")


def handle_literal_declaration(identifier_type, init, name, tokens, variables):
    identifier = Identifier(name, str_to_cast(init["value"], identifier_type),
                            str_to_type[identifier_type])
    tokens.append(identifier)
    variables[name] = identifier


def handle_identifier_declaration(init, name, tokens, variables):
    referenced_identifier = variables[init["name"]]
    identifier = Identifier(name, referenced_identifier.value, referenced_identifier.literal_type)
    tokens.append(identifier)
    variables[name] = identifier


def handle_empty_declaration(identifier_type, name, tokens, variables):
    identifier = Identifier(name, str_to_cast(None, identifier_type), str_to_type[identifier_type])
    tokens.append(identifier)
    variables[name] = identifier


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
