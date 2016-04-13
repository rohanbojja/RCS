import RPi.GPIO as GPIO
import time

def clk:
	#Stepper motor function here
def aclk:
    #Stepper motor function here

GPIO.setmode(GPIO.BOARD)
GPIO.setup(8,GPIO.OUT)#Stepper Motor
GPIO.setup(10,GPIO.OUT)#Stepper Motor
GPIO.setup(12,GPIO.OUT)#Stepper Motor
GPIO.setup(11,GPIO.OUT)#Stepper Motor
GPIO.setup(13,GPIO.OUT)#DeMux selector
GPIO.setup(15,GPIO.out)#DeMux selector
f = open("seqin.txt","r")
strin=f.read()#The string
strl=strin.split()#Converted to List
str2=strl[::-1]#Reversed the List

#Add selector pins appropriately
while(len(str2)):
	#Functions
	if(str2[0]=="R"):
		clk()
	elif(str2[0]=="L"):
		clk()
	elif(str2[0]=="D"):
		clk()
	elif(str2[0]=="F"):
		clk()
	elif(str2[0]=="T"):
		clk()
	elif(str2[0]=="B"):
		clk()
	#Primes
	elif(str2[0]=="R'"):
		aclk()
	elif(str2[0]=="L'"):
		aclk()
	elif(str2[0]=="D'"):
		aclk()
	elif(str2[0]=="F'"):
		aclk()
	elif(str2[0]=="T'"):
		aclk()
	elif(str2[0]=="B'"):
		aclk()	
	str2.pop()
GPIO.cleanup()
