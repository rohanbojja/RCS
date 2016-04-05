import RPi.GPIO as GPIO
import time

def clk(x):
	x.ChangeDutyCycle(12.5)
def aclk(x):
    x.ChangeDutyCycle(2.5)
    return cur
def reset(x):
	x.ChangeDutyCycle(7.5)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(8,GPIO.OUT)#Servo 1 Right
GPIO.setup(10,GPIO.OUT)#Servo 2 Left
GPIO.setup(12,GPIO.OUT)#Servo 3 Down
GPIO.setup(11,GPIO.OUT)#Servo 4 Front
GPIO.setup(13,GPIO.OUT)#Servo 5 Top
GPIO.setup(15,GPIO.OUT)#Servo 6 Back

r=GPIO.PWM(8,50)
l=GPIO.PWM(10,50)
d=GPIO.PWM(12,50)
f=GPIO.PWM(11,50)
t=GPIO.PWM(13,50)
b=GPIO.PWM(15,50)

r.start(7.5)
l.start(7.5)
d.start(7.5)
f.start(7.5)
t.start(7.5)
b.start(7.5)

f = open("seqin.txt","r")
strin=f.read()#The string
strl=strin.split()#Converted to List
str2=strl[::-1]#Reversed the List

while(len(str2)):
	#Functions
	if(str2[0]=="R"):
		clk(r)
	elif(str2[0]=="L"):
		clk(l)
	elif(str2[0]=="D"):
		clk(d)
	elif(str2[0]=="F"):
		clk(f)
	elif(str2[0]=="T"):
		clk(t)
	elif(str2[0]=="B"):
		clk(b)
	#Primes
	elif(str2[0]=="R'"):
		aclk(r)
	elif(str2[0]=="L'"):
		aclk(l)
	elif(str2[0]=="D'"):
		aclk(d)
	elif(str2[0]=="F'"):
		aclk(f)
	elif(str2[0]=="T'"):
		aclk(t)
	elif(str2[0]=="B'"):
		aclk(b)	
	str2.pop()
GPIO.cleanup()
