
from tkinter import Tk, Canvas



class Window():
    def __init__(self, width, height):
        self.window = Tk()
        self.window.title("boot.dev maze")
        # self.window.geometry(f"{width}x{height}")
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
