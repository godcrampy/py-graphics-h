from pycparser import CParser

from src.generate_tokens import tokenize_node, get_main_nodes
from src.parse_file import to_dict


def add_token(test_str, is_print=False):
    parser = CParser()
    ast = parser.parse(test_str)
    tokens = []
    nodes = get_main_nodes(to_dict(ast))
    for node in nodes:
        if is_print:
            print(node)
        token = tokenize_node(node)
        tokens.append(token)
    return tokens


def wrap_with_main(test_str):
    return f"int main() {{ {test_str} }}"
