from typing import List, Dict

from src.token.function_call import FunctionCall
from src.token.identifier import Identifier
from src.token.literal import Literal
from src.token.token import Token, LiteralType


def str_to_cast(value, type_str):
    if type_str == "int":
        return int(value) if value else int()
    if type_str == "string":
        return str(value) if value else int()
    return value


str_to_type: Dict[str, LiteralType] = {
    "int": LiteralType.INT,
    "string": LiteralType.STR
}


def generate_tokens(ast, variables: Dict[str, Identifier]):
    tokens: List[Token] = []
    # find main
    main_node = ast["ext"][0]
    main_node_items = main_node["body"]["block_items"]
    # generate token in main

    for node in main_node_items:
        node_type = node["_nodetype"]
        print(node_type)
        if node_type == "Decl":
            # new identifier (variable) is created
            name = node["name"]
            init = node["init"]
            identifier_type = node["type"]["type"]["names"][0]
            if init is None:
                # no RHS value
                identifier = Identifier(name, str_to_cast(None, identifier_type), str_to_type[identifier_type])
                tokens.append(identifier)
                variables[name] = identifier
                continue
            declaration_type = init["_nodetype"]
            if declaration_type == "ID":
                # RHS value is in variables
                identifier = Identifier(name, variables[init["name"]].value, variables[init["name"]].literal_type)
                tokens.append(identifier)
                variables[name] = identifier
            elif declaration_type == "Constant":
                # RHS value is literal
                identifier = Identifier(name, str_to_cast(init["value"], identifier_type), str_to_type[identifier_type])
                tokens.append(identifier)
                variables[name] = identifier
            else:
                raise Exception(f"Unexpected RHS of variable: {node['coord']}")
        elif node_type == "FuncCall":
            name = node["name"]["name"]
            args = node["args"]["exprs"]
            params = []
            for arg in args:
                node_type = arg["_nodetype"]
                if node_type == "Constant":
                    literal = Literal(arg["value"], str_to_type[arg["type"]])
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

    return tokens
