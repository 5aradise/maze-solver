from window import Window
from logic import *
from graphics import *


def main():
    win_width = 800
    win_height = 600
    win = Window(win_width, win_height)

    maze = Maze(Vec2(win_width/2 - 8 * 40, win_height/2 - 6 * 40), 16, 12, 40)
    maze.draw(win)

    win.wait_for_close()


main()
