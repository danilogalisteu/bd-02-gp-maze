
from window import Window
from maze import Maze


win = Window(800, 600)

m = Maze(50, 50, 10, 14, 50, 50, win)

m.solve()

win.wait_for_close()
