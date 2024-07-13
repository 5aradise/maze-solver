from window import Window
from logic import *
from graphics import *


def main():
    screen_width = 880
    screen_height = 660
    num_rows = 24
    num_cols = 32
    cell_size = 20

    win = Window(screen_width, screen_height)

    maze = Maze(Vec2((screen_width - num_cols*cell_size)/2,
                (screen_height - num_rows*cell_size)/2), num_cols, num_rows, cell_size)
    maze.draw(win)

    is_solveable = maze.solve(win)
    if not is_solveable:
        print("maze can not be solved!")
    else:
        print("maze solved!")

    win.wait_for_close()


main()
