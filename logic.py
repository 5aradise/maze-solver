import window
from graphics import *
from tkinter import Canvas


class Cell:
    def __init__(self,
                 pos: Vec2, size: float,
                 has_left_wall=True,
                 has_right_wall=True,
                 has_top_wall=True,
                 has_bottom_wall=True) -> None:
        self.pos = pos
        self.l_wall = has_left_wall
        self.r_wall = has_right_wall
        self.t_wall = has_top_wall
        self.b_wall = has_bottom_wall
        self.__lines = [
            Line(pos, pos+Vec2(size, 0)),
            Line(pos+Vec2(size, 0), pos+Vec2(size, size)),
            Line(pos+Vec2(0, size), pos+Vec2(size, size)),
            Line(pos, pos+Vec2(0, size)),
        ]

    def draw(self, canvas: Canvas, color: str) -> None:
        if self.t_wall:
            self.__lines[0].draw(canvas, color)
        
        if self.r_wall:
            self.__lines[1].draw(canvas, color)

        if self.b_wall:
            self.__lines[2].draw(canvas, color)

        if self.l_wall:
            self.__lines[3].draw(canvas, color)
