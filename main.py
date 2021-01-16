import json
import os
from typing import Dict

from dotenv import load_dotenv
from easygraphics import Color, easy_run

from src.execute_tokens import execute_tokens
from src.generate_tokens import generate_tokens
from src.parse_file import get_ast

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

variables: Dict[str, any] = {
    # VGA Modes
    "VGALO": 0,
    "VGAMED": 1,
    "VGAHI": 2,
    "VGAMAX": 3,
    "VGA640": 4,
    "VGA800": 5,
    "VGA1024": 6,
    # VGA Drivers
    "VGA": 9,
    "DETECT": 0,
    "USER": 0,
    # Colors
    "BLACK": 0,
    "BLUE": 1,
    "GREEN": 2,
    "CYAN": 3,
    "RED": 4,
    "MAGENTA": 5,
    "BROWN": 6,
    "LIGHTGRAY": 7,
    "DARKGRAY": 8,
    "LIGHTBLUE": 9,
    "LIGHTGREEN": 10,
    "LIGHTCYAN": 11,
    "LIGHTRED": 12,
    "LIGHTMAGENTA": 13,
    "YELLOW": 14,
    "WHITE": 15,
    "__text_color__": Color.WHITE
}

tokens = generate_tokens(ast)


# print([token.__str__() for token in tokens])
# print(variables)
def main():
    execute_tokens(tokens, variables)


easy_run(main)
