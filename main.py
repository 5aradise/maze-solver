from window import Window
from logic import *
from graphics import *


def main():
    win_width = 1600
    win_height = 1200
    win = Window(win_width, win_height)

    maze = Maze(Vec2(win_width/2 - 8 * 70, win_height/2 - 6 * 70), 16, 12, 70)
    maze.draw(win)

    win.wait_for_close()


main()
