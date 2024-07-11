from window import Window
from logic import *
from graphics import *


def main():
    win = Window(800, 600)

    c1 = Cell(Vec2(50, 50), 50)
    c1.r_wall = False
    win.draw_obj(c1)

    c2 = Cell(Vec2(100, 50), 50)
    c2.l_wall = False
    c2.b_wall = False
    win.draw_obj(c2)

    win.draw_obj(c1.move(c2))

    c3 = Cell(Vec2(100, 100), 50)
    c3.t_wall = False
    c3.r_wall = False
    win.draw_obj(c3)

    win.draw_obj(c2.move(c3))

    c4 = Cell(Vec2(150, 100), 50)
    c4.l_wall = False
    win.draw_obj(c4)

    win.draw_obj(c3.move(c4, True))

    win.wait_for_close()


main()
