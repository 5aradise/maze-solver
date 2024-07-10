from window import Window
from graphics import *
from logic import *


def main():
    win = Window(800, 600)

    c1 = Cell(Vec2(50, 50), 50)
    c1.l_wall = False
    win.draw_obj(c1)

    c2 = Cell(Vec2(125, 125), 75)
    c2.r_wall = False
    win.draw_obj(c2)

    c3 = Cell(Vec2(225, 225), 25)
    c3.t_wall = False
    win.draw_obj(c3)

    c4 = Cell(Vec2(300, 300), 200)
    c4.b_wall = False
    win.draw_obj(c4)

    win.wait_for_close()


main()
