from typing import Dict, List, Set, Tuple

from easygraphics import Color, set_caption, set_color, set_fill_color, draw_rect, set_font_size, get_color, draw_text, \
    arc, fill_rect, draw_line, draw_polygon, get_fill_color, draw_ellipse, \
    draw_circle, draw_pie, clear_device, get_width, get_height, pause

from src.packages.package import Package

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

color_to_int: Dict[Color, int] = {
    Color.BLACK: 0,
    Color.BLUE: 1,
    Color.GREEN: 2,
    Color.CYAN: 3,
    Color.RED: 4,
    Color.MAGENTA: 5,
    Color.BROWN: 6,
    Color.LIGHT_GRAY: 7,
    Color.DARK_GRAY: 8,
    Color.LIGHT_BLUE: 9,
    Color.LIGHT_GREEN: 10,
    Color.LIGHT_CYAN: 11,
    Color.LIGHT_RED: 12,
    Color.LIGHT_MAGENTA: 13,
    Color.YELLOW: 14,
    Color.WHITE: 15,
}


class GraphicsPackage(Package):
    @classmethod
    def get_supported_functions(cls) -> Set[str]:
        return {"initgraph", "getchar", "getch", "closegraph", "outtextxy", "setcolor", "setfontcolor", "arc", "bar",
                "bar3d",
                "line", "rectangle",
                "ellipse", "fillellipse", "fillcircle", "drawpoly", "fillpoly", "getfontcolor", "pieslice", "sector",
                "circle", "cleardevice", "getmaxx", "getmaxy"}

    @classmethod
    def execute(cls, name: str, variables: Dict[str, any], args: List):
        text_color_key = "__text_color__"
        if name == "initgraph":
            graph_mode = args[1]
            # init_graph(*(int_to_vga_modes[graph_mode]))
            set_caption("pycc")
            set_color(Color.BLACK)
            set_fill_color(Color.BLACK)
            draw_rect(0, 0, get_width(), get_height())
            set_color(Color.WHITE)
            set_font_size(15)
            set_fill_color(Color.TRANSPARENT)
            variables[text_color_key] = 15
            return 0
        if name == "getchar" or name == "getch":
            pause()
            return 0
        if name == "closegraph":
            # close_graph()
            return 0
        if name == "outtextxy":
            x = args[0]
            y = args[1]
            text = args[2]
            temp_color = get_color()
            set_color(int_to_color[variables[text_color_key]])
            draw_text(x, y + 10, text)
            set_color(temp_color)
            return 0
        if name == "setcolor":
            color = int_to_color[args[0]]
            set_color(color)
            return 0
        if name == "setfontcolor":
            variables[text_color_key] = args[0]
            return 0
        if name == "arc":
            x = args[0]
            y = args[1]
            s = args[2]
            e = args[3]
            r = args[4]
            arc(x, y, s + 360, e + 360, r, r)
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
        if name == "bar3d":
            print("Function bar3d not supported")
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
        if name == "fillcircle":
            x = args[0]
            y = args[1]
            r = args[2]
            temp_color = get_fill_color()
            set_fill_color(get_color())
            draw_circle(x, y, r)
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
        if name == "getfontcolor":
            return variables[text_color_key]
        if name == "pieslice":
            x = args[0]
            y = args[1]
            s = args[2]
            e = args[3]
            r = args[4]
            draw_pie(x, y, s, e, r, r)
            return 0
        if name == "sector":
            x = args[0]
            y = args[1]
            s = args[2]
            e = args[3]
            r1 = args[4]
            r2 = args[5]
            draw_pie(x, y, s, e, r1, r2)
            return 0
        if name == "circle":
            x = args[0]
            y = args[1]
            r = args[2]
            draw_circle(x, y, r)
            return 0
        if name == "cleardevice":
            clear_device()
            return 0
        if name == "getmaxx":
            return get_width()
        if name == "getmaxy":
            return get_height()
        raise Exception(f"Function {name} not in Graphics Package")
