#Generates the sequence of moves to be performed
#Reads the current faces from "fin.txt"
import numpy as np
#1 - white, 2 - red, 3 - yellow, 4 - orange, 5 - blue, 6 - green
#		ARRAY REPRESENTATION OF THE CUBE
#		le^		top^			ri^
#	[a][b][c]	[a][b][c]	[a][b][c]
#	[d][e][f]	[d][e][f]	[d][e][f]
#	[g][h][i]	[g][h][i]	[g][h][i]
#	 Bot^		front^ 		Back^
#	[c][b][a]	[a][b][c]	[c][b][a]
#	[f][e][d]	[d][e][f]	[f][e][b]
#	[i][h][g]	[g][h][i]	[i][h][c]

swap = np.array([['a','b','c'], ['d','e','f'], ['g','h','i']])	#Temporary Array
top = np.array([['a','b','c'], ['d','e','f'], ['a','b','c']])
front = np.array([['a','b','c'], ['d','e','f'], ['g','h','i']])
bot = np.array([['a','b','c'], ['d','e','f'], ['g','h','i']])
back = np.array([['a','b','c'], ['d','e','f'], ['g','h','i']])
ri = np.array([['a','b','c'], ['d','e','f'], ['d','e','f']])
le = np.array([['a','b','c'], ['d','e','f'], ['j','k','l']])
#INITIALIZE THE CUBE HERE
#
#
#
#Predefined moves
def F(): #Set the front face
	"Rotate front by +90 deg."
	x=0
	while(x<3):
		swap[2][x]=top[2][x]
		top[2][x]=le[2][x]
		le[2][x]=bot[2][x]
		bot[2][x]=ri[2][x]
		ri[2][x]=swap[2][x]
		x=x+1
	#Rotating the front face +90 deg.
	#CAN BE USED FOR ROTATING ANY FACE
	#Fixed
	x=0
	y=0
	while(x<3):
		y=0
		while(y<3):
			swap[x][y]=front[x][y]
			y=y+1
		x=x+1
	x1=0#Row
	y1=0#Column
	x2=2
	y2=0
	while(x1<3):
		y1=0
		x2=2
		while(y1<3):
			front[x1][y1]=swap[x2][y2]
			y1=y1+1
			x2=x2-1
		y2=y2+1
		x1=x1+1
	return
	return
	
def Fp(): #Set the front face
	"Rotate front by -90 deg."
	x=0
	while(x<3):
		swap[2][x]=top[2][x]
		top[2][x]=ri[2][x]
		ri[2][x]=bot[2][x]
		bot[2][x]=le[2][x]
		le[2][x]=swap[2][x]
		x=x+1
	#Rotating the front face
	#CAN BE USED FOR ROTATING ANY FACE
	#Fixed
	x=0
	y=0
	while(x<3):
		y=0
		while(y<3):
			swap[x][y]=front[x][y]
			y=y+1
		x=x+1
	x1=0#Row
	y1=0#Column
	x2=0
	y2=2
	while(x1<3):
		y1=0
		x2=0
		while(y1<3):
			front[x1][y1]=swap[x2][y2]
			y1=y1+1
			x2=x2+1
		y2=y2-1
		x1=x1+1
	return
#print all the faces
def paf():
	print "Top: "
	print top
	print "Front: "
	print front
	print "Bot: "
	print bot
	print "Back: "
	print back
	print "Right: "
	print ri
	print  "Left: "
	print le
	print"\n"*2
	return
	
#Solving part
paf()
F()
Fp()
paf()