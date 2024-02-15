
from window import Window
from maze import Maze


win = Window(800, 600)

m = Maze(50, 50, 10, 10, 50, 50, win)

win.wait_for_close()
