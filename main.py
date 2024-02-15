
from tkinter import Tk, Canvas
from graphics import Point, Line
from cell import Cell



class Window():
    def __init__(self, width, height):
        self.window = Tk()
        self.window.title("boot.dev maze")
        self.window.geometry(f"{width}x{height}")
        self.window.protocol("WM_DELETE_WINDOW", self.close)
        self.canvas = Canvas(self.window, width=width, height=height)
        self.canvas.pack()
        self.running = False
    
    def redraw(self):
        self.window.update_idletasks()
        self.window.update()

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()

    def close(self):
        self.running = False
    
    def draw_line(self, line, fill_color):
        line.draw(self.canvas, fill_color)


win = Window(800, 600)

l1 = Line(Point(600, 10), Point(50, 450))
win.draw_line(l1, 'red')

l2 = Line(Point(10, 10), Point(700, 500))
win.draw_line(l2, 'blue')

c1 = Cell(200, 200, 250, 250, win)
c1.draw()

c2 = Cell(300, 300, 350, 350, win)
c2.has_bottom_wall = False
c2.draw()

c3 = Cell(400, 400, 450, 450, win)
c3.has_top_wall = False
c3.has_left_wall = False
c3.draw()

c4 = Cell(500, 500, 550, 550, win)
c4.has_right_wall = False
c4.has_left_wall = False
c4.draw()

c1.draw_move(c2)

c3.draw_move(c4, undo=True)

win.wait_for_close()
