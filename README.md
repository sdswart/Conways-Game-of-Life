# Conways-Game-of-Life

<img src="https://github.com/sdswart/Conways-Game-of-Life/blob/master/Conway.JPG" alt="Conway">
Graphical implementation of the game of life with tkinter

Requires Python 3+ with numpy, tkinter, math and scipy

<h1>Background</h1>

I created this script mainly to improve my skills in tkinter and numpy. It utilizes tkinter to create a checkered canvas to run Conway's Game of Life. Live cells can be created by clicking and draging across the canvas. The code can also be stopped and started, and the time between updates changed via GUI controls.

<h1>To run the program</h1>

<strong>python conway.py</strong>
<br>
This will open the tkinter window. Look under other windows if it doesn't start at the top.

<h1>To begin the game of life</h1>
<ul><li>Select the starting cells by clicking or dragging the canvas</li>
<li>Click the start button</li></ul>

The height and width of the canvas, as well as the size of the cells can be changed by adding the optional arguments:<br>
  <ul><li>-h, --help            to show help </li>
  <li>-height <value> or --height <value> to change Canvas height</li>
  <li>-width <value> or --width <value> to change Canvas width</li>
  <li>-size <value> or --size <value> to change the size of the cells</li></ul>

Example: python conway.py --size 5  (this will make the size of the cells smaller -> default size = 10)
