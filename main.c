#include "graphics.h"

int main(int argc, char const *argv[]) {
  int gdriver = DETECT + 5;
  int gmode = VGAMAX;
  gmode = 5;
//  int x = 20;
//  int y = 20;
//  int incr_y = 50;
  int dppoints[14] = {200, 150, 300, 250, 400, 150, 425,
                      350, 300, 275, 150, 350, 200, 150};
//  int fppoints[14] = {500, 150, 600, 250, 700, 150, 725,
//                      350, 600, 275, 450, 350, 500, 150};
//
  initgraph(&gdriver, &gmode, "");
//
//  outtextxy(x, y, "Arc");
//  setcolor(RED);
//  arc(x + 80, y, -5, 20, 45);
//  y += incr_y;
//
//  outtextxy(x, y, "Bar");
//  setcolor(GREEN);
//  bar(x + 80, y, x + 120, y + 20);
//  y += incr_y;
//
//  setcolor(YELLOW);
//  outtextxy(x, y, "Line");
//  line(x + 80, y, x + 120, y + 10);
//  y += incr_y;
//
//  setcolor(BLUE);
//  outtextxy(x, y, "Rectangle");
//  rectangle(x + 80, y, x + 120, y + 10);
//  y += incr_y;
//
//  setcolor(WHITE);
//  outtextxy(x, y, "Ellipse");
//  ellipse(x + 100, y + 5, 0, 360, 30, 10);
//  y += incr_y;
//
//  drawpoly(7, dppoints);
//  setcolor(RED);
//  fillpoly(7, fppoints);
//
//  setcolor(YELLOW);
//  outtextxy(x, y, "Filled Ellipse");
//  fillellipse(x + 150, y + 5, 30, 10);
//  y += incr_y;
//
//  setfontcolor(GREEN);
//  outtextxy(x, y, "Green Text");
//
//
//  getchar();
  closegraph();
//  return 0;
}
