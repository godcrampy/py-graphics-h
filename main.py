import json
import os
from typing import Dict

from dotenv import load_dotenv
from easygraphics import easy_run

from src.execute_tokens import execute_tokens
from src.generate_tokens import generate_tokens
from src.parse_file import get_ast
from src.token.identifier import Identifier
from src.token.token import LiteralType

load_dotenv()

debug = os.getenv("DEBUG") == "TRUE"

file_name = "main.c"
if debug:
    print(f"Opening file: {file_name}")
ast = get_ast(file_name)

if debug:
    print(f"File parsed...")
    tree_file_name = "tree.json"
    with open(tree_file_name, 'w', encoding='utf-8') as f:
        print(f"Saved to {tree_file_name}")
        json.dump(ast, f, indent=2)

variables: Dict[str, Identifier] = {
    # VGA Modes
    "VGALO": Identifier("VGALO", 0, LiteralType.INT),
    "VGAMED": Identifier("VGAMED", 1, LiteralType.INT),
    "VGAHI": Identifier("VGAHI", 2, LiteralType.INT),
    "VGAMAX": Identifier("VGAMAX", 3, LiteralType.INT),
    "VGA640": Identifier("VGA640", 4, LiteralType.INT),
    "VGA800": Identifier("VGA800", 5, LiteralType.INT),
    "VGA1024": Identifier("VGA1024", 6, LiteralType.INT),
    # VGA Drivers
    "VGA": Identifier("VGA", 9, LiteralType.INT),
    "DETECT": Identifier("DETECT", 0, LiteralType.INT),
    "USER": Identifier("USER", 0, LiteralType.INT),
    # Colors
    "BLACK": Identifier("BLACK  ", 0, LiteralType.INT),
    "BLUE": Identifier("BLUE", 1, LiteralType.INT),
    "GREEN": Identifier("GREEN", 2, LiteralType.INT),
    "CYAN": Identifier("CYAN", 3, LiteralType.INT),
    "RED": Identifier("RED", 4, LiteralType.INT),
    "MAGENTA": Identifier("MAGENTA", 5, LiteralType.INT),
    "BROWN": Identifier("BROWN", 6, LiteralType.INT),
    "LIGHTGRAY": Identifier("LIGHTGRAY", 7, LiteralType.INT),
    "DARKGRAY": Identifier("DARKGRAY", 8, LiteralType.INT),
    "LIGHTBLUE": Identifier("LIGHTBLUE", 9, LiteralType.INT),
    "LIGHTGREEN": Identifier("LIGHTGREEN", 10, LiteralType.INT),
    "LIGHTCYAN": Identifier("LIGHTCYAN", 11, LiteralType.INT),
    "LIGHTRED": Identifier("LIGHTRED", 12, LiteralType.INT),
    "LIGHTMAGENTA": Identifier("LIGHTMAGENTA", 13, LiteralType.INT),
    "YELLOW": Identifier("YELLOW", 14, LiteralType.INT),
    "WHITE": Identifier("WHITE", 15, LiteralType.INT),
}

tokens = generate_tokens(ast)


# print([token.__str__() for token in tokens])
# print(variables)
def main():
    execute_tokens(tokens)


easy_run(main)
