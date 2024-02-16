# bd-02-gp-maze

Guided project:
> Build a visual maze solver using Python and Tkinter. You'll be writing code that draws a randomized maze and then systematically solves it. You will use your knowledge of algorithms to automate this fun game! This is a fantastic way to build a real project and solidify your algorithmic skills.

Steps:
* set up environment
  * WSL Ubuntu
  * Python 3.12 with pyenv
  * VS Code
* verify/install `tkinter` and dependencies
  * `python -m tkinter`
  * `sudo apt-get install tk-dev`
  * had to uninstall and reinstall python for it to recognize tk
* create Tk window class
* create point and line classes, draw lines on canvas
* create cell class, draw cells on canvas
* draw moves from cell to cell
* create maze class
  * member cell array
  * method to initialize cells
  * method to draw cells with animation (delay)
* create maze init tests with `unittest`
* draw openings at entrance and exit
* new cell member `visited`
* new maze method to break walls randomly
  * walk depth first from entrance
  * choose random wall to break
* new recursive maze method to solve maze
  * walk depth first from entrance
  * check for broken walls to move in all unvisited directions
  * undo moves when there is no exit
