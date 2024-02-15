
from graphics import Point, Line



class Cell():
    def __init__(self, x1, y1, x2, y2, window=None):
        self._xt = min(x1, x2)
        self._xb = max(x1, x2)
        self._xc = (x1 + x2) / 2
        self._yl = min(y1, y2)
        self._yr = max(y1, y2)
        self._yc = (y1 + y2) / 2
        self._win = window
        self.has_top_wall = True
        self.has_right_wall = True
        self.has_bottom_wall = True
        self.has_left_wall = True

    def draw(self, wall_color="black", open_color="white"):
        if self._win is None:
            return

        ptl = Point(self._xt, self._yl)
        ptr = Point(self._xt, self._yr)
        pbr = Point(self._xb, self._yr)
        pbl = Point(self._xb, self._yl)

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
