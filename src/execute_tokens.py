from typing import List, Dict, Tuple

from easygraphics import *

from src.token.token import Token

int_to_vga_modes: Dict[int, Tuple[int, int]] = {
    0: (640, 200),
    1: (640, 350),
    2: (640, 480),
    3: (800, 600),
    4: (640, 480),
    5: (800, 600),
    6: (1024, 768),
}

int_to_color: Dict[int, Color] = {
    0: Color.BLACK,
    1: Color.BLUE,
    2: Color.GREEN,
    3: Color.CYAN,
    4: Color.RED,
    5: Color.MAGENTA,
    6: Color.BROWN,
    7: Color.LIGHT_GRAY,
    8: Color.DARK_GRAY,
    9: Color.LIGHT_BLUE,
    10: Color.LIGHT_GREEN,
    11: Color.LIGHT_CYAN,
    12: Color.LIGHT_RED,
    13: Color.LIGHT_MAGENTA,
    14: Color.YELLOW,
    15: Color.WHITE,
}

text_color = Color.WHITE


def execute_tokens(tokens: List[Token], variables: Dict[str, any]):
    for token in tokens:
        token.eval(variables)
