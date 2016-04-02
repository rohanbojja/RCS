#BOJJA, Do not edit this till I'm done.
#code from inter.py copied.
import RPi.GPIO as GPIO
import time
#clk is the function for clockwise rotation of servo
#aclk is for anti-clockwise rotation.Obviously.
def clk(x):
	x.ChangeDutyCycle(12.5)
def aclk(x):
    x.ChangeDutyCycle(2.5)
    return cur
def reset(x):
	x.ChangeDutyCycle(7.5)
#Uncomment the below functions
def og('d'):
	#open gripper here
def cg('d'):
	#close gripper here
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)#Servo 1 Right
GPIO.setup(13,GPIO.OUT)#Servo 2 Left
GPIO.setup(15,GPIO.OUT)#Servo 3 Bot
r=GPIO.PWM(11,50)#1
d=GPIO.PWM(13,50)#2
l=GPIO.PWM(15,50)#3
r.start(7.5)#init all three
d.start(7.5)
l.start(7.5)
curr=curl=curd=7.5
#time.sleep(1)
f = open("seqin.txt","r")
strin=f.read()#The string
strl=strin.split()#Converted to List
str2=strl[::-1]#Reversed the List
#Going through the list
while(len(str2)):
    if(str2[0]=="R"):
		clk(r)
		og('r')
		reset(r)
		cg('r')
	if(str2[0]=="R'"):
		aclk(r)
		og('r')
		reset(r)
		cg('r')
	if(str2[0]=="L'"):
		aclk(l)
		og('l')
		reset(l)
		cg('l')
	if(str2[0]=="L"):
		clk(l)
		og('l')
		reset(l)
		cg('l')
		#
	if(str2[0]=="D"):
		og('l')
		clk(l)
		cg('l')
		og('r')
		clk(r)
		cg('r')
		clk(d)
		og('d')
		reset(d)
		cg('d')
		og('l')
		reset(l)
		cg('l')
		og('r')
		reset(r)
		cg('r')
	if(str2[0]=="D'"):
		og('l')
		clk(l)
		cg('l')
		og('r')
		clk(r)
		cg('r')
		aclk(d)
		og('d')
		reset(d)
		cg('d')
		og('l')
		reset(l)
		cg('l')
		og('r')
		reset(r)
		cg('r')
	if(str2[0]=="F"):
		og('d')
		#Simultaenous rotation of both left(clk) and right(aclk) arms bitches
		cg('d')
		clk(d)
		og('d')
		reset(d)
		#Simultaenous rotation of both left(aclk) and right(clk) arms bitches
		cg('d')
	if(str2[0]=="F'"):
		og('d')
		#Simultaenous rotation of both left(clk) and right(aclk) arms bitches
		cg('d')
		aclk(d)
		og('d')
		reset(d)
		#Simultaenous rotation of both left(aclk) and right(clk) arms bitches
		cg('d')
	if(str2[0]=="U"):
		og('d')
		#Simultaenous rotation of both left(clk) and right(aclk) arms bitches
		cg('d')
		og('l')
		og('r')
		#Simultaenous rotation of both left(aclk) and right(clk) arms bitches
		cg('l')
		cg('r')
		og('d')
		#Simultaenous rotation of both left(clk) and right(aclk) arms bitches
		clk(d)
		og('d')
		reset(d)
		#Simultaenous rotation of both left(aclk) and right(clk) arms bitches
		og('l')
		og('r')
		#Simultaenous rotation of both left(clk) and right(aclk) arms bitches
		cg('l')
		cg('r')
		#Simultaenous rotation of both left(aclk) and right(clk) arms bitches
		cg('d')
	if(str2[0]=="U'"):
		og('d')
		#Simultaenous rotation of both left(clk) and right(aclk) arms bitches
		cg('d')
		og('l')
		og('r')
		#Simultaenous rotation of both left(aclk) and right(clk) arms bitches
		cg('l')
		cg('r')
		og('d')
		#Simultaenous rotation of both left(clk) and right(aclk) arms bitches
		aclk(d)
		og('d')
		reset(d)
		#Simultaenous rotation of both left(aclk) and right(clk) arms bitches
		og('l')
		og('r')
		#Simultaenous rotation of both left(clk) and right(aclk) arms bitches
		cg('l')
		cg('r')
		#Simultaenous rotation of both left(aclk) and right(clk) arms bitches
		cg('d')
	if(str2[0]=="B"):
		og('d')
		#Simultaenous rotation of both left(aclk) and right(clk) arms bitches
		cg('d')
		clk(d)
		og('d')
		reset(d)
		#Simultaenous rotation of both left(clk) and right(aclk) arms bitches
		cg('d')
	if(str2[0]=="B'"):
		og('d')
		#Simultaenous rotation of both left(aclk) and right(clk) arms bitches
		cg('d')
		aclk(d)
		og('d')
		reset(d)
		#Simultaenous rotation of both left(clk) and right(aclk) arms bitches
		cg('d')
	str2.pop()
GPIO.cleanup()