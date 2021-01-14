#include "graphics.h"

int main(int argc, char *argv[]) {
  int gdriver = DETECT;
  int gmode = VGAMAX;

  initgraph(&gdriver, &gmode, "");
  outtextxy(20, 20, "Sahil");

  setcolor(RED);
  line(0, 0, 1024, 768);

  setcolor(BLUE);
  circle(50, 50, 20);

  setcolor(YELLOW);
  arc(100, 100, 0, 45, 78);

  setcolor(BROWN);
  rectangle(25, 25, 75, 75);

  getchar();
  closegraph();
  return 0;
}
