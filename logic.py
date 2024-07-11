from graphics import *
from tkinter import Canvas
import theme


class Cell(Drawable):
    def __init__(self,
                 pos: Vec2, size: float,
                 has_left_wall=True,
                 has_right_wall=True,
                 has_top_wall=True,
                 has_bottom_wall=True) -> None:
        self.l_wall = has_left_wall
        self.r_wall = has_right_wall
        self.t_wall = has_top_wall
        self.b_wall = has_bottom_wall
        self._pos = pos
        self._size = size
        self.__body = [
            Line(pos, pos+Vec2(size, 0), theme.CELL_COLOR),
            Line(pos+Vec2(size, 0), pos+Vec2(size, size), theme.CELL_COLOR),
            Line(pos+Vec2(0, size), pos+Vec2(size, size), theme.CELL_COLOR),
            Line(pos, pos+Vec2(0, size), theme.CELL_COLOR),
        ]

    def draw(self, canvas: Canvas) -> None:
        if self.t_wall:
            self.__body[0].draw(canvas)

        if self.r_wall:
            self.__body[1].draw(canvas)

        if self.b_wall:
            self.__body[2].draw(canvas)

        if self.l_wall:
            self.__body[3].draw(canvas)

    def move(self, to_cell: 'Cell', undo=False) -> tuple[Line, str]:
        start = self._pos + Vec2(self._size/2, self._size/2)
        end = to_cell._pos + Vec2(to_cell._size/2, to_cell._size/2)
        move = Line(
            start, end, theme.PATH_COLOR if not undo else theme.PATH_UNDO_COLOR)
        return move
