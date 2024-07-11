import unittest

from logic import Maze
from graphics import Vec2


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m = Maze(Vec2(0, 0), num_cols, num_rows,  10)
        self.assertEqual(
            len(m._cells[0]),
            num_cols,
        )
        self.assertEqual(
            len(m._cells),
            num_rows,
        )

    def test_maze_row_size_equality(self):
        num_cols = 12
        m = Maze(Vec2(0, 0), num_cols, 10,  10)
        for row in m._cells:
            self.assertEqual(len(row), num_cols)

    def test_maze_cells_pos(self):
        cell_size = 17
        start_x = 3
        start_y = 87
        m = Maze(Vec2(start_x, start_y), 100, 100,  cell_size)
        self.assertEqual(
            m._cells[50][50]._pos,
            Vec2(start_x + 50 * cell_size, start_y + 50 * cell_size),
        )
        self.assertEqual(
            m._cells[34][0]._pos,
            Vec2(start_x + 0 * cell_size, start_y + 34 * cell_size),
        )
        self.assertEqual(
            m._cells[98][99]._pos,
            Vec2(start_x + 99 * cell_size, start_y + 98 * cell_size),
        )


if __name__ == "__main__":
    unittest.main()
