"""
@author: Stephen
"""
#%% Imports
from tkinter import *
import numpy as np
import math
import scipy.signal
import argparse

#%% Variables
RepeatConway = False
canvas_width = 300
canvas_height = 300 
line_distance = 10
ConwaySpeed=500

#%% Get command line arguments
def main():
    global canvas_width
    global canvas_height
    global line_distance
    parser = argparse.ArgumentParser(description='Conways game of life by Stephen')
    parser.add_argument("-height","--height", help='Canvas height', default=300)
    parser.add_argument("-width","--width", help='Canvas width', default=300)
    parser.add_argument("-size","--size", help='Cell size', default=10)
    args = vars(parser.parse_args())
    
    canvas_width=int(args['width'])
    canvas_height=int(args['height'])
    line_distance=int(args['size'])

if __name__ == "__main__":
    main()

# initialize array
ConwayMatrix = np.zeros((int(math.floor(canvas_width/line_distance)),int(math.floor(canvas_height/line_distance))),dtype=np.int)

#%% checkered definition
def checkered(canvas, line_distance):
   # vertical lines at an interval of "line_distance" pixel
   for x in range(line_distance,canvas_width,line_distance):
      canvas.create_line(x, 0, x, canvas_height, fill="#C6C6C6")
   # horizontal lines at an interval of "line_distance" pixel
   for y in range(line_distance,canvas_height,line_distance):
      canvas.create_line(0, y, canvas_width, y, fill="#C6C6C6")

#%% Colour block
def LiveBlock(x,y):
    global canvas
    x,y = x*line_distance, y*line_distance
    canvas.create_rectangle(x,y,x+line_distance,y+line_distance,fill = "#000000",outline="#C6C6C6")

def DeadBlock(x,y):
    global canvas
    x,y = x*line_distance, y*line_distance
    canvas.create_rectangle(x,y,x+line_distance,y+line_distance,fill = "#FFFFFF",outline="#C6C6C6")
    
#%% Click event
def callback(event):
    global ConwayMatrix
    x1, y1 = ( event.x - 1 ), ( event.y - 1 )
    x1=math.floor(x1/line_distance)
    y1=math.floor(y1/line_distance)
    ConwayMatrix[x1,y1]=1
    LiveBlock(x1,y1)
    
#%% Update grid
def updategrid(NewMatrix):
    global ConwayMatrix
    it = np.nditer(NewMatrix, flags=['multi_index'])
    while not it.finished:
        if NewMatrix[it.multi_index] != ConwayMatrix[it.multi_index]:
            if NewMatrix[it.multi_index]==0:
                DeadBlock(it.multi_index[0],it.multi_index[1])
            else:
                LiveBlock(it.multi_index[0],it.multi_index[1])
        it.iternext()

#%% Factions to update Game of Life
def Conway():
    global ConwayMatrix
    global root
    global RepeatConway
    global ConwaySpeed
    ConwaySpeed=slider.get()
    NewMatrix=scipy.signal.convolve2d(ConwayMatrix, np.ones((3,3)), mode='same')-ConwayMatrix
    def rules(Current, Neighbours):
        if Current ==1 and Neighbours<2:
            return 0
        elif Current ==1 and Neighbours in (2,3):
            return 1
        elif Current ==1 and Neighbours > 3:
            return 0
        elif Current ==0 and Neighbours==3:
            return 1
        else:
            return 0
    vfunc = np.vectorize(rules)
    NewMatrix=vfunc(ConwayMatrix,NewMatrix)
    NewMatrix.astype(int)
    updategrid(NewMatrix)
    ConwayMatrix=NewMatrix
    if RepeatConway: root.after(ConwaySpeed, Conway)
    
def SwitchConway():
    global RepeatConway
    global button1
    if RepeatConway:
        button1.config(text='Start')
        RepeatConway=False
    else:
        button1.config(text='Stop')
        RepeatConway=True
        Conway()
    
#%% Start Canvas with Game of Life
root = Tk()
canvas = Canvas(root, width=canvas_width, height=canvas_height)
canvas.config(background="#FFFFFF")
canvas.pack()

checkered(canvas,line_distance)
canvas.bind("<B1-Motion>", callback)
canvas.bind("<Button-1>", callback)

slider = Scale(root, from_=10, to=2000, orient=HORIZONTAL, label="Delay:",length=canvas_width)
slider.pack()
slider.set(ConwaySpeed)

button1 = Button(root, text = "Start", command = SwitchConway, anchor = W)
button1.configure(width = 10, activebackground = "#33B5E5", relief = RAISED)
button1_window = canvas.create_window(canvas_width, canvas_height+25, anchor=SE, window=button1)
print('Starting the game of life window. Close it to stop the program.')

mainloop()
