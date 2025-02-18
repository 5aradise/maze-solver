from tkinter import Tk, BOTH, Canvas
import theme


class Window:
    def __init__(self, width: int = 800, height: int = 600) -> None:
        root = Tk()
        root.title("Maze solver")
        root.protocol("WM_DELETE_WINDOW", self.close)
        canvas = Canvas(root, bg=theme.BACKGROUND_COLOR,
                        width=width, height=height)
        canvas.pack(fill=BOTH, expand=1)

        self.__root = root
        self.__canvas = canvas
        self.__running = False

    @property
    def canvas(self):
        return self.__canvas

    def redraw(self):
        self.__root.update()
        self.__root.update_idletasks()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()

    def close(self):
        self.__running = False
