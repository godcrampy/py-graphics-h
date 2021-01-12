import json
import os
from typing import Dict

from dotenv import load_dotenv

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
    "VGA": Identifier("VGA", 9, LiteralType.INT),
    "DETECT": Identifier("DETECT", 0, LiteralType.INT)
}

tokens = generate_tokens(ast, variables)

print([token.__str__() for token in tokens])
print(variables)
