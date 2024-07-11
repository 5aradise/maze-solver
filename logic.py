from graphics import *
from window import Window
import theme
import time


class Maze:
    def __init__(self,
                 pos: Vec2,
                 num_cols: int,
                 num_rows: int,
                 cell_size: float) -> None:
        self.pos = pos
        self.num_cols = num_cols
        self.num_rows = num_rows
        self.cell_size = cell_size
        self._cells = list[list[Cell]]()
        self._create_cells()

    def _create_cells(self):
        curr_pos = self.pos.copy()
        for _ in range(self.num_rows):
            cell_row = list[Cell]()
            for _ in range(self.num_cols):
                cell_row.append(Cell(curr_pos.copy(), self.cell_size))
                curr_pos += Vec2(self.cell_size, 0)
            self._cells.append(cell_row)
            curr_pos.x = self.pos.x
            curr_pos.y += self.cell_size

    def draw(self, win: Window):
        for cell_row in self._cells:
            for cell in cell_row:
                cell.draw(win)
                win.redraw()
                time.sleep(0.02)


class Cell:
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

    def draw(self, win: Window) -> None:
        if self.t_wall:
            self.__body[0].draw(win)

        if self.r_wall:
            self.__body[1].draw(win)

        if self.b_wall:
            self.__body[2].draw(win)

        if self.l_wall:
            self.__body[3].draw(win)

    def move(self, to_cell: 'Cell', undo=False) -> tuple[Line, str]:
        start = self._pos + Vec2(self._size/2, self._size/2)
        end = to_cell._pos + Vec2(to_cell._size/2, to_cell._size/2)
        move = Line(
            start, end, theme.PATH_COLOR if not undo else theme.PATH_UNDO_COLOR)
        return move
