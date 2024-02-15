
from time import sleep

from cell import Cell



class Maze():
    def __init__(
        self, x0, y0,
        num_rows, num_cols,
        cell_size_x, cell_size_y,
        window=None,
    ):
        self.x0 = x0
        self.y0 = y0
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._win = window
        self._cells = [[None for i in range(self.num_cols)] for j in range(self.num_rows)]
        self._create_cells()

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
