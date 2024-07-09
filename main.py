from window import Window
from graphics import *


def main():
    win = Window(800, 600)

    line1 = Line(Vec2(10, 10), Vec2(90, 90))
    win.draw_line(line1)

    line2 = Line(Vec2(90, 10), Vec2(10, 90))
    win.draw_line(line2)

    win.wait_for_close()


main()
