#Generates the sequence of moves to be performed
#Reads the current faces from "fin.txt"

import numpy as np#Fix numpy
#1 - white, 2 - red, 3 - yellow, 4 - orange, 5 - blue, 6 - green
#cube faces
top = np.full((3,3),1)
front = np.full((3,3),2)
bot = np.full((3,3),3)
back = np.full((3,3),4)
ri = np.full((3,3),5)
le = np.full((3,3),6)
#Algorithms

#all faces
print top
print front
print bot
print back
print ri
print le