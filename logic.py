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
        self.solve_delay = 0.03

        self._cells = list[list[Cell]]()
        self.entrance = (0, 0)
        self.exit = (self.num_rows-1, self.num_cols-1)

        self.__to_draws = list[Drawable]()

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
        entrance = self._cells[self.entrance[0]][self.entrance[1]]
        entrance.l_wall = False
        self.__to_draws.append(entrance.copy())
        exit = self._cells[self.exit[0]][self.exit[1]]
        exit.r_wall = False
        self.__to_draws.append(exit.copy())

    def _create_maze(self):
        entrance = self._cells[self.entrance[0]][self.entrance[1]]
        entrance.visited = True
        self._create_maze_r(entrance, self.entrance[0], self.entrance[1])
        self._reset_visiting()

    def _create_maze_r(self, start_cell: 'Cell', start_i: int, start_j: int):
        to_visit = [None for i in range(4)]
        if 0 <= start_j-1 and not self._cells[start_i][start_j-1].visited:
            to_visit[0] = (self._cells[start_i][start_j-1])

        if 0 <= start_i-1 and not self._cells[start_i-1][start_j].visited:
            to_visit[1] = (self._cells[start_i-1][start_j])

        if start_j+1 < self.num_cols and not self._cells[start_i][start_j+1].visited:
            to_visit[2] = (self._cells[start_i][start_j+1])

        if start_i+1 < self.num_rows and not self._cells[start_i+1][start_j].visited:
            to_visit[3] = (self._cells[start_i+1][start_j])

        visited_neigh = 0
        while visited_neigh != 4:
            visited_neigh = 0

            if to_visit[0] and not to_visit[0].visited:
                if random.randint(0, 2) == 0:
                    visited_neigh += 1
                    l_cell = to_visit[0]
                    l_cell.visited = True
                    start_cell.l_wall = False
                    l_cell.r_wall = False
                    self.__to_draws.append(start_cell)
                    self.__to_draws.append(l_cell)
                    self._create_maze_r(l_cell, start_i, start_j-1)
            else:
                visited_neigh += 1

            if to_visit[1] and not to_visit[1].visited:
                if random.randint(0, 2) == 0:
                    visited_neigh += 1
                    t_cell = to_visit[1]
                    t_cell.visited = True
                    start_cell.t_wall = False
                    t_cell.b_wall = False
                    self.__to_draws.append(start_cell)
                    self.__to_draws.append(t_cell)
                    self._create_maze_r(t_cell, start_i-1, start_j)
            else:
                visited_neigh += 1

            if to_visit[2] and not to_visit[2].visited:
                if random.randint(0, 2) == 0:
                    visited_neigh += 1
                    r_cell = to_visit[2]
                    r_cell.visited = True
                    start_cell.r_wall = False
                    r_cell.l_wall = False
                    self.__to_draws.append(start_cell)
                    self.__to_draws.append(r_cell)
                    self._create_maze_r(r_cell, start_i, start_j+1)
            else:
                visited_neigh += 1

            if to_visit[3] and not to_visit[3].visited:
                if random.randint(0, 2) == 0:
                    visited_neigh += 1
                    b_cell = self._cells[start_i+1][start_j]
                    b_cell.visited = True
                    start_cell.b_wall = False
                    b_cell.t_wall = False
                    self.__to_draws.append(start_cell)
                    self.__to_draws.append(b_cell)
                    self._create_maze_r(b_cell, start_i+1, start_j)
            else:
                visited_neigh += 1

    def _reset_visiting(self):
        for row in self._cells:
            for cell in row:
                cell.visited = False

    def solve(self, win: Window) -> bool:
        entrance = self._cells[self.entrance[0]][self.entrance[1]]
        entrance.l_wall = True
        is_solveable = self._solve_r(
            entrance, self.entrance[0], self.entrance[1], win)
        entrance.l_wall = False
        self._reset_visiting()
        return is_solveable

    def _solve_r(self, curr_cell: 'Cell', curr_i: int, curr_j: int, win: Window) -> bool:
        if curr_i == self.exit[0] and curr_j == self.exit[1]:
            return True
        curr_cell.visited = True

        if not curr_cell.r_wall:
            r_cell = self._cells[curr_i][curr_j+1]
            if not r_cell.visited:
                curr_cell.move(r_cell).draw(win)
                win.redraw()
                time.sleep(self.solve_delay)
                is_exit = self._solve_r(r_cell, curr_i, curr_j+1, win)
                if is_exit:
                    return True
                else:
                    curr_cell.move(r_cell, True).draw(win)

        if not curr_cell.b_wall:
            b_cell = self._cells[curr_i+1][curr_j]
            if not b_cell.visited:
                curr_cell.move(b_cell).draw(win)
                win.redraw()
                time.sleep(self.solve_delay)
                is_exit = self._solve_r(b_cell, curr_i+1, curr_j, win)
                if is_exit:
                    return True
                else:
                    curr_cell.move(b_cell, True).draw(win)

        if not curr_cell.l_wall:
            l_cell = self._cells[curr_i][curr_j-1]
            if not l_cell.visited:
                curr_cell.move(l_cell).draw(win)
                win.redraw()
                time.sleep(self.solve_delay)
                is_exit = self._solve_r(l_cell, curr_i, curr_j-1, win)
                if is_exit:
                    return True
                else:
                    curr_cell.move(l_cell, True).draw(win)

        if not curr_cell.t_wall:
            t_cell = self._cells[curr_i-1][curr_j]
            if not t_cell.visited:
                curr_cell.move(t_cell).draw(win)
                win.redraw()
                time.sleep(self.solve_delay)
                is_exit = self._solve_r(t_cell, curr_i-1, curr_j, win)
                if is_exit:
                    return True
                else:
                    curr_cell.move(t_cell, True).draw(win)

        return False

    def draw(self, win: Window):
        for to_draw in self.__to_draws:
            to_draw.draw(win)
            win.redraw()
            time.sleep(0.005)


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

    def move(self, to_cell: 'Cell', undo=False) -> Line:
        start = self._pos + Vec2(self._size/2, self._size/2)
        end = to_cell._pos + Vec2(to_cell._size/2, to_cell._size/2)
        move = Line(
            start, end, theme.PATH_COLOR if not undo else theme.PATH_UNDO_COLOR)
        return move
