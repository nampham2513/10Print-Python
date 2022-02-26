# C64 10Print Drawing on Modern PC
# Inspired by The Coding Train and 8-Bit Show and Tell

import time
from tkinter import *
from random import randint

resWidth = 1200
resHeight = 800
lineLength = 20
lineThick = 4
timeStep = 0.0083
isPressed = False

print('Time per line:', (float(resWidth) / lineLength) * timeStep, 'secs')
print('Time to draw canvas:', (float(resWidth) / lineLength) * timeStep * (float(resHeight) / lineLength), 'secs')

print()
print('Click on the drawing window to stop drawing')

def drawLine(num, numx, numy):
	global lineLength
	 
	if (num % 2) == 0:
		canv.create_line(numx, numy, numx + lineLength, numy + lineLength, width = lineThick)
		
	else:
		canv.create_line(numx, numy + lineLength, numx + lineLength, numy, width = lineThick)
		
def drawCanvas():
	global resHeight, resWidth, isPressed

	posx = 0
	posy = 0
	
	while isPressed == False:
		for posy in range(0, resHeight, lineLength):
			if isPressed == True:
				return
		
			for posx in range(0, resWidth, lineLength):
				num = randint(0, 1)
				drawLine(num, posx, posy)
				canv.update()
				
				time.sleep(timeStep)
		
		time.sleep(1.5)
		canv.delete('all')
		
def on_canv_click(event):
	global isPressed

	#print('Hey!', event)
	isPressed = True
			
root = Tk()

canv = Canvas(root, width = resWidth, height = resHeight, background = 'gray')
canv.bind('<Button-1>', on_canv_click)
canv.pack()

drawCanvas()

root.mainloop()
