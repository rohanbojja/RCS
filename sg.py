#Generates the sequence of moves to be performed
#Reads the current faces from "fin.txt"
import numpy as np
#w - white, r - red, y - yellow, o - orange, b - blue, g - green
#^ - a^
#		ARRAY REPRESENTATION OF THE CUBE
#		le^		top^			ri^
#	[a][b][c]	[a][b][c]	[a][b][c]
#	[d][e][f]	[d][e][f]	[d][e][f]
#	[g][h][i]	[g][h][i]	[g][h][i]
#	 Bot^		front^ 		Back^
#	[c][b][a]	[a][b][c]	[c][b][a]
#	[f][e][d]	[d][e][f]	[f][e][b]
#	[i][h][g]	[g][h][i]	[i][h][c]
#
#		CUBE RELATIONS
#	bot[0][1] - back[2][1]	EDGE
#	bot[1][0] - ri[1][2]	EDGE
#	bot[1][2] - le[1][0]	EDGE
#	bot[2][1] - front[2][1]	EDGE
#
#
#
#
#
#
#	Rep when top is on top:
#							top
#					left	front	right	back
#							bot
#	Rep when top is on top:
#							bot
#					right	front	left	back	
#							top

swap = np.array([['a','b','c'], ['d','e','f'], ['a','b','c']]) #Temporary Array
front = np.array([['y','r','o'], ['r','r','w'], ['y','r','g']])
top = np.array([['w','b','w'], ['g','b','g'], ['b','y','y']])
le = np.array([['g','o','o'], ['y','w','r'], ['r','b','r']])
bot = np.array([['w','g','o'], ['o','g','b'], ['o','w','g']]) #This will have the cross
ri = np.array([['r','g','r'], ['y','y','w'], ['b','b','y']])
back = np.array([['b','o','b'], ['w','o','y'], ['g','o','w']]) 
#INITIALIZE THE CUBE HERE
#
#
#
#Predefined moves
sequence=[]
def F(): #Set the front face
	"Rotate front by +90 deg."
	sequence.append("F")
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
	sequence.append("Fp")
	x=0
	while(x<3):
		swap[2][x]=top[2][x]
		top[2][x]=ri[2][x]
		ri[2][x]=bot[2][x]
		bot[2][x]=le[2][x]
		le[2][x]=swap[2][x]
		x=x+1
	#Rotating the front face -90 deg.
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
#Cross check YET TO BE IMPLEMENTED
def cross_check():
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
#Check edges for a color
def fe( ec ):
	return

#Solving part
paf()
#Cross on bot
	#Generate Centers

#First layer
#Second layer
#Boom


#Output Generation
