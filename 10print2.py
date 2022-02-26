# C64 10Print Drawing on Modern PC
# Inspired by The Coding Train and 8-Bit Show and Tell

import time
from tkinter import *
from random import randint

resWidth = 600
resHeight = resWidth
lineLength = 20
timeStep = 0.03

def drawLine(num, numx, numy):
	global lineLength
	 
	if (num % 2) == 0:
		canv.create_line(numx, numy, numx + lineLength, numy + lineLength, width = 4)
		
	else:
		canv.create_line(numx, numy + lineLength, numx + lineLength, numy, width = 4)
		
#canv.create_line(0, 0, 20, 20, width = 2)
#canv.create_line(20, 20, 40, 0, width = 2)

#canv.create_line(posx, posy, posx + 20, posy + 20, width = 2) #0
#posx += 20
#canv.create_line(posx, posy + 20, posx + 20, 0, width = 2) #1

def drawCanvas():
	global resHeight, resWidth

	posx = 0
	posy = 0
	
	while True:
		for posy in range(0, resHeight, lineLength):
			for posx in range(0, resWidth, lineLength):
				num = randint(0, 1)
				drawLine(num, posx, posy)
				canv.update()
				
				time.sleep(timeStep)
		
		time.sleep(1.5)
		canv.delete('all')
		
def on_canv_click(event):
	root.destroy()
			
root = Tk()

canv = Canvas(root, width = resWidth, height = resHeight, background = 'gray')
canv.bind('<Button-1>', on_canv_click)
canv.pack()

drawCanvas()

root.mainloop()
