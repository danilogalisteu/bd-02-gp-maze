
from time import sleep
import random

from cell import Cell



class Maze():
    def __init__(
        self, x0, y0,
        num_rows, num_cols,
        cell_size_x, cell_size_y,
        window=None, seed=None,
    ):
        self.x0 = x0
        self.y0 = y0
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._win = window

        self._cells = [
            [None for j in range(self.num_rows)]
            for i in range(self.num_cols)
        ]

        if seed is not None:
            random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

    def _create_cells(self):
        x0i = self.x0
        for i in range(self.num_cols):
            y0j = self.y0
            for j in range(self.num_rows):
                self._cells[i][j] = Cell(
                    x0i,
                    y0j,
                    x0i+self.cell_size_x,
                    y0j+self.cell_size_y,
                    self._win
                )
                self._draw_cell(i, j)
                y0j += self.cell_size_y
            x0i += self.cell_size_x

    def _draw_cell(self, i, j):
        self._cells[i][j].draw()
        self._animate()
    
    def _animate(self, sleep_time=0.05):
        if self._win is None:
            return

        self._win.redraw()
        sleep(sleep_time)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._cells[0][0].draw()
        self._cells[-1][-1].has_bottom_wall = False
        self._cells[-1][-1].draw()
    
    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            to_visit = []
            if i > 0:
                if not self._cells[i-1][j].visited:
                    to_visit.append(('l', i-1, j))
            if j > 0:
                if not self._cells[i][j-1].visited:
                    to_visit.append(('u', i, j-1))
            if i < self.num_cols - 1:
                if not self._cells[i+1][j].visited:
                    to_visit.append(('r', i+1, j))
            if j < self.num_rows - 1:
                if not self._cells[i][j+1].visited:
                    to_visit.append(('d', i, j+1))

            if not to_visit:
                self._cells[i][j].draw()
                return

            to_next = to_visit[random.randrange(len(to_visit))]
            if to_next[0] == 'l':
                self._cells[i][j].has_left_wall = False
                self._cells[i-1][j].has_right_wall = False
            elif to_next[0] == 'u':
                self._cells[i][j].has_top_wall = False
                self._cells[i][j-1].has_bottom_wall = False
            elif to_next[0] == 'r':
                self._cells[i][j].has_right_wall = False
                self._cells[i+1][j].has_left_wall = False
            elif to_next[0] == 'd':
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j+1].has_top_wall = False

            self._cells[i][j].draw()
            self._break_walls_r(to_next[1], to_next[2])

    def _reset_cells_visited(self):
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._cells[i][j].visited = False
