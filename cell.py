
from graphics import Point, Line



class Cell():
    def __init__(self, x1, y1, x2, y2, window=None):
        self._xl = min(x1, x2)
        self._xr = max(x1, x2)
        self._xc = (x1 + x2) / 2
        self._yt = min(y1, y2)
        self._yb = max(y1, y2)
        self._yc = (y1 + y2) / 2
        self._win = window
        self.has_top_wall = True
        self.has_right_wall = True
        self.has_bottom_wall = True
        self.has_left_wall = True

    def draw(self, wall_color="black", open_color="#d9d9d9"):
        if self._win is None:
            return

        ptl = Point(self._xl, self._yt)
        ptr = Point(self._xr, self._yt)
        pbr = Point(self._xr, self._yb)
        pbl = Point(self._xl, self._yb)

        if self.has_top_wall:
            self._win.draw_line(Line(ptl, ptr), wall_color)
        else:
            self._win.draw_line(Line(ptl, ptr), open_color)
        if self.has_right_wall:
            self._win.draw_line(Line(ptr, pbr), wall_color)
        else:
            self._win.draw_line(Line(ptr, pbr), open_color)
        if self.has_bottom_wall:
            self._win.draw_line(Line(pbr, pbl), wall_color)
        else:
            self._win.draw_line(Line(pbr, pbl), open_color)
        if self.has_left_wall:
            self._win.draw_line(Line(pbl, ptl), wall_color)
        else:
            self._win.draw_line(Line(pbl, ptl), open_color)

    def draw_move(self, to_cell, undo=False):
        if self._win is None:
            return

        p1 = Point(self._xc, self._yc)
        p2 = Point(to_cell._xc, to_cell._yc)

        line = Line(p1, p2)
        line.draw(
            self._win.canvas,
            "gray" if undo else "red",
        )
