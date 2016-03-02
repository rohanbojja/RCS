#Generates the sequence of moves to be performed
#Reads the current faces from "fin.txt"
import numpy as np
#1 - white, 2 - red, 3 - yellow, 4 - orange, 5 - blue, 6 - green
#cube faces

#	[G][G][G]	[W][W][W]	[B][B][B]
#	[G][G][G]	[W][W][W]	[B][B][B]
#	[G][G][G]	[W][W][W]	[B][B][B]

#	[R][R][R]	[O][O][O]	[Y][Y][Y]
#	[R][R][R]	[O][O][O]	[Y][Y][Y]
#	[R][R][R]	[O][O][O]	[Y][Y][Y]

swap = np.full((3,3),0)			#Temporary Array
top = np.full((3,3),1)		#White	-	top
front = np.full((3,3),2)	#Red	-	Front
bot = np.full((3,3),3)		#Yellow	-	Bot
back = np.full((3,3),4)		#Orange	-	Back
ri = np.full((3,3),5)		#Blue	-	Right
le = np.full((3,3),6)		#Green	-	Left
#Predefined moves
def F(): #Set the front face
	"Rotate front by 90 deg."
	x=0
	while(x<3):
		swap[2][x] = top[2][x]
		top[2][x] = le[2][x]
		le[2][x] = bot[2][x]
		bot[2][x] = ri[2][x]
		ri[2][x] = swap[2][x]
		x=x+1
	#Rotating the front face
	x=0
	y=2
	while(x<3): #Fix this
		swap[0][x] = front[0][x]
		front[0][x] = front[y][0]
		front[2][x] = front[y][2]
		front[y][2] = swap[0][x]
		x=x+1
		y=y-1
	return

def Fp(): #Set the front face
	"Rotate front by -90 deg."
	x=0
	while(x<3):
		swap[2][x] = top[2][x]
		top[2][x] = ri[2][x]
		le[2][x] = top[2][x]
		bot[2][x] = le[2][x]
		ri[2][x] = swap[2][x]
		x=x+1
	return

#print all the faces
def paf():
	print top
	print
	print front
	print
	print bot
	print
	print back
	print
	print ri
	print
	print le
	print"\n"*2
	return
	
#Solving part
F()
paf()
Fp()
paf()