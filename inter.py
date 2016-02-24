#Interprets the moves in "seqin.txt" in this directory.
f = open("seqin.txt","r")
strin=f.read()#The string
strl=strin.split()#Converted to List
str2=strl[::-1]#Reversed the List
print str2

#Going through the list
while(len(str2)):
	print str2[len(str2)-1]#REPLACE THIS WITH THE ACTUAL THING, Hardware Interaction
	str2.pop()
