
import unittest

from maze import Maze



class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_create_cells_large(self):
        num_cols = 40
        num_rows = 30
        m1 = Maze(0, 0, num_rows, num_cols, 20, 20)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_entrance_exit(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertFalse(
            m1._cells[0][0].has_top_wall,
        )
        self.assertFalse(
            m1._cells[num_cols-1][num_rows-1].has_bottom_wall,
        )

    def test_maze_clear_visited(self):
        num_cols = 14
        num_rows = 10
        m1 = Maze(50, 50, num_rows, num_cols, 50, 50, seed=42)

        for i in range(num_cols):
            for j in range(num_rows):
                self.assertEqual(
                    m1._cells[i][j].visited,
                    False,
                )


if __name__ == "__main__":
    unittest.main()
