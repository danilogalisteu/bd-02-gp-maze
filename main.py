
from tkinter import Tk, Canvas
from graphics import Point, Line



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

win.wait_for_close()
