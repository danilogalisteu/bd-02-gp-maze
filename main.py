
from tkinter import Tk, Canvas
from maze import Maze


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

m = Maze(50, 50, 10, 10, 50, 50, win)

win.wait_for_close()
