from tkinter import Tk, BOTH, Canvas
from graphics import *


class Window:
    def __init__(self, title: str, width: int = 800, height: int = 600) -> None:
        root = Tk()
        root.title("Maze solver")
        root.protocol("WM_DELETE_WINDOW", self.close)
        canvas = Canvas(root, bg="black",
                        width=width, height=height)
        canvas.pack(fill=BOTH, expand=1)

        self.__root = root
        self.__canvas = canvas
        self.__running = False

    def redraw(self):
        self.__root.update()
        self.__root.update_idletasks()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()

    def close(self):
        self.__running = False

    def draw_line(self, line: Line, color: str = "white"):
        line.draw(self.__canvas, color)
