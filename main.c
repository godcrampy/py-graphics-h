#include "graphics.h"

int main(int argc, char const *argv[]) {
  int gdriver = DETECT;
  int gmode = VGAMAX;
  int x = 20;
  int y = 20;
  int incr_y = 50;
  int dppoints[14] = {y, 150, 300, 250, 400, 150, 425,
                      350, 300, 275, 150, 350, 200, 150};

  initgraph(&gdriver, &gmode, "");

  outtextxy(x, y, "Arc");
  setcolor(RED);
  arc(x + 80, y, -5, 20, 45);
  y += incr_y;

  outtextxy(x, y, "Bar");
  setcolor(GREEN);
  bar(x + 80, y, x + 120, y + 20);
  y += incr_y;

  setcolor(YELLOW);
  outtextxy(x, y, "Line");
  line(x + 80, y, x + 120, y + 10);
  y += incr_y;

  setcolor(BLUE);
  outtextxy(x, y, "Rectangle");
  rectangle(x + 80, y, x + 120, y + 10);
  y += incr_y;

  setcolor(WHITE);
  outtextxy(x, y, "Ellipse");
  ellipse(x + 100, y + 5, 0, 360, 30, 10);
  y += incr_y;

  // drawpoly(2, {{1, 2}, {40, 5}});

  getchar();
  closegraph();
  return 0;
}
