# Conways-Game-of-Life
Graphical implementation of the game of life with tkinter

Requires Python 3+ with numpy, tkinter, math and scipy

Background
I created this script mainly to improve my skills in tkinter and numpy. It utilizes tkinter to create a checkered canvas to run Conway's Game of Life. Live cells can be created by clicking and draging across the canvas. The code can also be stopped and started, and the time between updates changed via GUI controls.

To run the program run the following:
python conway.py

This will open the tkinter window. Look under other windows if it doesn't start at the top.

To begin the game of life:
1) Select the starting cells by clicking or dragging the canvas
2) Click the start button

The height and width of the canvas, as well as the size of the cells can be changed by adding the optional arguments:
  -h, --help            to show help 
  -height <value> or --height <value> to change Canvas height
  -width <value> or --width <value> to change Canvas width
  -size <value> or --size <value> to change the size of the cells

Example: python conway.py --size 5  (this will make the size of the cells smaller -> default size = 10)
