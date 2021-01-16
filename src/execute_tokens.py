from typing import List, Dict, Tuple

from easygraphics import *

from src.token.function_call import FunctionCall
from src.token.literal import Literal
from src.token.token import Token, LiteralType

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


def execute_tokens(tokens: List[Token]):
    for token in tokens:
        if isinstance(token, FunctionCall):
            execute_function_call(token)


def execute_function_call(token):
    params = token.params
    # print(token.name, [p.__str__() for p in params])
    if token.name == "initgraph":
        graph_mode = token.params[1].value
        init_graph(*(int_to_vga_modes[graph_mode]))
        set_caption("main.c")
        set_color(Color.BLACK)
        set_fill_color(Color.BLACK)
        draw_rect(0, 0, *(int_to_vga_modes[graph_mode]))
        set_color(Color.WHITE)
        set_font_size(15)
        set_fill_color(Color.TRANSPARENT)
        return Literal(0, LiteralType.VOID)
    if token.name == "outtextxy":
        x = params[0].value
        y = params[1].value
        text = params[2].value
        temp_color = get_color()
        global text_color
        set_color(text_color)
        draw_text(x, y + 10, text)
        set_color(temp_color)
        return Literal(0, LiteralType.VOID)
    if token.name == "setfontcolor":
        color = int_to_color[params[0].value]
        text_color = color
        return Literal(0, LiteralType.VOID)
    if token.name == "line":
        x1 = params[0].value
        y1 = params[1].value
        x2 = params[2].value
        y2 = params[3].value
        draw_line(x1, y1, x2, y2)
        return Literal(0, LiteralType.VOID)
    if token.name == "arc":
        x = params[0].value
        y = params[1].value
        s = params[2].value
        e = params[3].value
        r = params[4].value
        arc(x, y, s, e, r, r)
        return Literal(0, LiteralType.VOID)
    if token.name == "ellipse":
        x = params[0].value
        y = params[1].value
        s = params[2].value
        e = params[3].value
        r1 = params[4].value
        r2 = params[5].value
        arc(x, y, s, e, r1, r2)
        return Literal(0, LiteralType.VOID)
    if token.name == "fillellipse":
        x = params[0].value
        y = params[1].value
        r1 = params[2].value
        r2 = params[3].value
        temp_color = get_fill_color()
        set_fill_color(get_color())
        draw_ellipse(x, y, r1, r2)
        set_fill_color(temp_color)
        return Literal(0, LiteralType.VOID)
    if token.name == "circle":
        x = params[0].value
        y = params[1].value
        r = params[2].value
        circle(x, y, r)
        return Literal(0, LiteralType.VOID)
    if token.name == "rectangle":
        x1 = params[0].value
        y1 = params[1].value
        x2 = params[2].value
        y2 = params[3].value
        draw_rect(x1, y1, x2, y2)
        return Literal(0, LiteralType.VOID)
    if token.name == "drawpoly":
        v = params[1].value
        draw_polygon(*v)
        return Literal(0, LiteralType.VOID)
    if token.name == "fillpoly":
        v = params[1].value
        temp_color = get_fill_color()
        set_fill_color(get_color())
        draw_polygon(*v)
        set_fill_color(temp_color)
        return Literal(0, LiteralType.VOID)
    if token.name == "bar":
        x1 = params[0].value
        y1 = params[1].value
        x2 = params[2].value
        y2 = params[3].value
        set_fill_color(get_color())
        fill_rect(x1, y1, x2, y2)
        set_fill_color(Color.BLACK)
        return Literal(0, LiteralType.VOID)
    if token.name == "setcolor":
        color = int_to_color[params[0].value]
        set_color(color)
        return Literal(0, LiteralType.VOID)
    if token.name == "getchar":
        pause()
        return Literal(0, LiteralType.VOID)
    if token.name == "closegraph":
        close_graph()
        return Literal(0, LiteralType.VOID)
    return Literal(0, LiteralType.VOID)
