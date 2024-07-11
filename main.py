from window import Window
from logic import *
from graphics import *


def main():
    win = Window(1600, 1200)

    maze = Maze(Vec2(10, 10), 16, 12, 70)
    maze.draw(win)

    win.wait_for_close()


main()
