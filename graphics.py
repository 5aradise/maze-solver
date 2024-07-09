import tkinter


class Vec2:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y


class Line:
    def __init__(self, p1: Vec2, p2: Vec2) -> None:
        self.p1 = p1
        self.p2 = p2

    def draw(self, canvas: tkinter.Canvas, color: str):
        canvas.create_line(self.p1.x, self.p1.y,
                           self.p2.x, self.p2.y, fill=color, width=2)
