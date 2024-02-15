


class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line():
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def draw(self, canvas, fill_color):
        canvas.create_line(
            self.p1.x, self.p1.y,
            self.p2.x, self.p2.y,
            fill=fill_color, width=2,
        )
        canvas.pack()


class Cell():
    def __init__(self, x1, y1, x2, y2, window):
        self._xt = min(x1, x2)
        self._xb = max(x1, x2)
        self._yl = min(y1, y2)
        self._yr = max(y1, y2)
        self._win = window
        self.has_top_wall = True
        self.has_right_wall = True
        self.has_bottom_wall = True
        self.has_left_wall = True

    def draw(self):
        p1 = Point(self._xt, self._yl)
        p2 = Point(self._xt, self._yr)
        p3 = Point(self._xb, self._yr)
        p4 = Point(self._xb, self._yl)
        lt = Line(p1, p2)
        lr = Line(p2, p3)
        lb = Line(p3, p4)
        ll = Line(p4, p1)
        if self.has_top_wall:
            self._win.draw_line(lt, 'black')
        if self.has_right_wall:
            self._win.draw_line(lr, 'black')
        if self.has_bottom_wall:
            self._win.draw_line(lb, 'black')
        if self.has_left_wall:
            self._win.draw_line(ll, 'black')
