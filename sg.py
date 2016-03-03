#Generates the sequence of moves to be performed
#Reads the current faces from "fin.txt"
import numpy as np
#INITIALIZE THE CUBE HERE
#1 - white, 2 - red, 3 - yellow, 4 - orange, 5 - blue, 6 - green
#		ARRAY REPRESENTATION OF THE CUBE
#		le->		top^		<-ri
#	[g][d][a]	[a][b][c]	[a][d][g]
#	[h][e][b]	[d][e][f]	[b][e][h]
#	[i][f][c]	[g][h][i]	[c][f][i]
#	 Bot->		front^ 		Back^
#	[i][f][c]	[a][b][c]	[c][b][a]
#	[h][e][b]	[d][e][f]	[f][e][b]
#	[g][d][a]	[g][h][i]	[i][h][c]

swap = np.array([['a','b','c'], ['d','e','f'], ['g','h','i']])	#Temporary Array
#top = np.full((3,3),1)		#White	-	top
#front = np.full((3,3),2)	#Red	-	Front
#bot = np.full((3,3),3)		#Yellow	-	Bot
#back = np.full((3,3),4)	#Orange	-	Back
#ri = np.full((3,3),5)		#Blue	-	Right
#le = np.full((3,3),6)		#Green	-	Left
top = np.array([['a','b','c'], ['d','e','f'], ['g','h','i']])
front = np.array([['a','b','c'], ['d','e','f'], ['g','h','i']])
bot = np.array([['a','b','c'], ['d','e','f'], ['g','h','i']])
back = np.array([['a','b','c'], ['d','e','f'], ['g','h','i']])
ri = np.array([['a','b','c'], ['d','e','f'], ['g','h','i']])
le = np.array([['a','b','c'], ['d','e','f'], ['g','h','i']])
#Predefined moves
def F(): #Set the front face
	"Rotate front by 90 deg."
	x=0
	while(x<3):
		swap[2][x] = top[2][x]
		top[2][x] = le[x][2]#Fixed
		le[x][2] = bot[2-x][0]#Fixed
		bot[2][x] = ri[2][x]#BROKEN
		ri[x][0] = swap[2][x]#POSSIBLY BROKEN
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
	#Rotating the front face by -90 deg.
	#FIX THIS
	swap[0][0]=front[0][0]
	front[0][0]=front[0][2]
	front[0][1]=front[1][2]
	front[0][2]=front[2][2]
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
paf()