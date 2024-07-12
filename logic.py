from graphics import *
from window import Window
import theme
import time
import random


class Drawable:
    def draw():
        pass


class Maze:
    def __init__(self,
                 pos: Vec2,
                 num_cols: int,
                 num_rows: int,
                 cell_size: float,
                 seed=None) -> None:
        self.pos = pos
        self.num_cols = num_cols
        self.num_rows = num_rows
        self.cell_size = cell_size
        self.__to_draws = list[Drawable]()
        self._cells = list[list[Cell]]()
        random.seed(seed)
        self._create_cells()
        self._create_entrance_and_exit()
        self._create_maze()

    def _create_cells(self):
        curr_pos = self.pos.copy()
        for _ in range(self.num_rows):
            cell_row = list[Cell]()
            for _ in range(self.num_cols):
                cell = Cell(curr_pos.copy(), self.cell_size)
                self.__to_draws.append(cell.copy())
                cell_row.append(cell)
                curr_pos += Vec2(self.cell_size, 0)
            self._cells.append(cell_row)
            curr_pos.x = self.pos.x
            curr_pos.y += self.cell_size

    def _create_entrance_and_exit(self):
        self._cells[0][0].l_wall = False
        self.__to_draws.append(self._cells[0][0].copy())
        self._cells[-1][-1].r_wall = False
        self.__to_draws.append(self._cells[-1][-1].copy())

    def _create_maze(self):
        self._cells[0][0].visited = True
        self._create_maze_r(0, 0)
        self._reset_visiting()

    def _create_maze_r(self, start_i: int, start_j: int):
        start_cell = self._cells[start_i][start_j]
        visited_neigh = 0
        while visited_neigh != 4:
            visited_neigh = 0

            if (0 <= start_j-1
                    and not self._cells[start_i][start_j-1].visited):
                if random.randint(0, 2) == 0:
                    visited_neigh += 1
                    l_cell = self._cells[start_i][start_j-1]
                    l_cell.visited = True
                    start_cell.l_wall = False
                    l_cell.r_wall = False
                    self.__to_draws.append(start_cell)
                    self.__to_draws.append(l_cell)
                    self._create_maze_r(start_i, start_j-1)
            else:
                visited_neigh += 1

            if (0 <= start_i-1
                    and not self._cells[start_i-1][start_j].visited):
                if random.randint(0, 2) == 0:
                    visited_neigh += 1
                    t_cell = self._cells[start_i-1][start_j]
                    t_cell.visited = True
                    start_cell.t_wall = False
                    t_cell.b_wall = False
                    self.__to_draws.append(start_cell)
                    self.__to_draws.append(t_cell)
                    self._create_maze_r(start_i-1, start_j)
            else:
                visited_neigh += 1

            if (start_j+1 <= self.num_cols-1
                    and not self._cells[start_i][start_j+1].visited):
                if random.randint(0, 2) == 0:
                    visited_neigh += 1
                    r_cell = self._cells[start_i][start_j+1]
                    r_cell.visited = True
                    start_cell.r_wall = False
                    r_cell.l_wall = False
                    self.__to_draws.append(start_cell)
                    self.__to_draws.append(r_cell)
                    self._create_maze_r(start_i, start_j+1)
            else:
                visited_neigh += 1

            if (start_i+1 <= self.num_rows-1
                    and not self._cells[start_i+1][start_j].visited):
                if random.randint(0, 2) == 0:
                    visited_neigh += 1
                    b_cell = self._cells[start_i+1][start_j]
                    b_cell.visited = True
                    start_cell.b_wall = False
                    b_cell.t_wall = False
                    self.__to_draws.append(start_cell)
                    self.__to_draws.append(b_cell)
                    self._create_maze_r(start_i+1, start_j)
            else:
                visited_neigh += 1

    def _reset_visiting(self):
        for row in self._cells:
            for cell in row:
                cell.visited = False

    def draw(self, win: Window):
        for to_draw in self.__to_draws:
            to_draw.draw(win)
            win.redraw()
            time.sleep(0.015)


class Cell:
    def __init__(self,
                 pos: Vec2, size: float,
                 has_left_wall=True,
                 has_right_wall=True,
                 has_top_wall=True,
                 has_bottom_wall=True,
                 visited=False) -> None:
        self.l_wall = has_left_wall
        self.r_wall = has_right_wall
        self.t_wall = has_top_wall
        self.b_wall = has_bottom_wall
        self.visited = visited
        self._pos = pos
        self._size = size
        self.__body = [
            Line(pos, pos+Vec2(size, 0), theme.CELL_COLOR),
            Line(pos+Vec2(size, 0), pos+Vec2(size, size), theme.CELL_COLOR),
            Line(pos+Vec2(0, size), pos+Vec2(size, size), theme.CELL_COLOR),
            Line(pos, pos+Vec2(0, size), theme.CELL_COLOR),
        ]

    def copy(self) -> 'Cell':
        return Cell(self._pos, self._size, self.l_wall, self.r_wall, self.t_wall, self.b_wall)

    def draw(self, win: Window) -> None:
        if self.t_wall:
            self.__body[0].color = theme.CELL_COLOR
        else:
            self.__body[0].color = theme.BACKGROUND_COLOR
        self.__body[0].draw(win)

        if self.r_wall:
            self.__body[1].color = theme.CELL_COLOR
        else:
            self.__body[1].color = theme.BACKGROUND_COLOR
        self.__body[1].draw(win)

        if self.b_wall:
            self.__body[2].color = theme.CELL_COLOR
        else:
            self.__body[2].color = theme.BACKGROUND_COLOR
        self.__body[2].draw(win)

        if self.l_wall:
            self.__body[3].color = theme.CELL_COLOR
        else:
            self.__body[3].color = theme.BACKGROUND_COLOR
        self.__body[3].draw(win)

    def move(self, to_cell: 'Cell', undo=False) -> tuple[Line, str]:
        start = self._pos + Vec2(self._size/2, self._size/2)
        end = to_cell._pos + Vec2(to_cell._size/2, to_cell._size/2)
        move = Line(
            start, end, theme.PATH_COLOR if not undo else theme.PATH_UNDO_COLOR)
        return move
