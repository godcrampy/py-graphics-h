from typing import List, Dict, Tuple

from easygraphics import init_graph, Color, set_caption, set_color, set_fill_color, draw_rect, set_font_size, pause, \
    close_graph, get_color, draw_text, arc, fill_rect, draw_line, draw_polygon, get_fill_color, draw_ellipse

from src.token.token import Token, TokenType

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


class FunctionCall(Token):
    def eval(self, variables: Dict[str, any]):
        args = []
        for param in self.params:
            args.append(param.eval(variables))

        return self.eval_func(args, variables)

    def eval_func(self, args: list, variables: Dict[str, any]):
        name = self.name
        text_color_key = "__text_color__"
        if name == "initgraph":
            graph_mode = args[1]
            init_graph(*(int_to_vga_modes[graph_mode]))
            set_caption("main.c")
            set_color(Color.BLACK)
            set_fill_color(Color.BLACK)
            draw_rect(0, 0, *(int_to_vga_modes[graph_mode]))
            set_color(Color.WHITE)
            set_font_size(15)
            set_fill_color(Color.TRANSPARENT)
            return 0
        if name == "getchar":
            pause()
            return 0
        if name == "closegraph":
            close_graph()
            return 0
        if name == "outtextxy":
            x = args[0]
            y = args[1]
            text = args[2]
            temp_color = get_color()
            set_color(variables[text_color_key])
            draw_text(x, y + 10, text)
            set_color(temp_color)
            return 0
        if name == "setcolor":
            color = int_to_color[args[0]]
            set_color(color)
            return 0
        if name == "setfontcolor":
            color = int_to_color[args[0]]
            variables[text_color_key] = color
            return 0
        if name == "arc":
            x = args[0]
            y = args[1]
            s = args[2]
            e = args[3]
            r = args[4]
            arc(x, y, s - 45, e - 45, r, r)
            return 0
        if name == "bar":
            x1 = args[0]
            y1 = args[1]
            x2 = args[2]
            y2 = args[3]
            set_fill_color(get_color())
            fill_rect(x1, y1, x2, y2)
            set_fill_color(Color.BLACK)
            return 0
        if name == "line":
            x1 = args[0]
            y1 = args[1]
            x2 = args[2]
            y2 = args[3]
            draw_line(x1, y1, x2, y2)
            return 0
        if name == "rectangle":
            x1 = args[0]
            y1 = args[1]
            x2 = args[2]
            y2 = args[3]
            draw_rect(x1, y1, x2, y2)
            return 0
        if name == "ellipse":
            x = args[0]
            y = args[1]
            s = args[2]
            e = args[3]
            r1 = args[4]
            r2 = args[5]
            arc(x, y, s, e, r1, r2)
            return 0
        if name == "fillellipse":
            x = args[0]
            y = args[1]
            r1 = args[2]
            r2 = args[3]
            temp_color = get_fill_color()
            set_fill_color(get_color())
            draw_ellipse(x, y, r1, r2)
            set_fill_color(temp_color)
            return 0
        if name == "drawpoly":
            v = args[1]
            draw_polygon(*v)
            return 0
        if name == "fillpoly":
            v = args[1]
            temp_color = get_fill_color()
            set_fill_color(get_color())
            draw_polygon(*v)
            set_fill_color(temp_color)
            return 0
        return 0

    def __init__(self, name: str, params: List[Token]):
        super().__init__(TokenType.FUNC_CALL)
        self.params = params
        self.name = name

    def __str__(self):
        return f"FunctionCall({self.name}, {[i.__str__() for i in self.params]})"
