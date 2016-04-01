#BOJJA, Do not edit this till I'm done.
#code from inter.py copied.
import RPi.GPIO as GPIO
import time
#clk is the function for clockwise rotation of servo
#aclk is for anti-clockwise rotation.Obviously.
def clk(x):
    x.ChangeDutyCycle(2.5)
def aclk(x):
    x.ChangeDutyCycle(12.5)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)#Servo 1 Left
GPIO.setup(13,GPIO.OUT)#Servo 2 Right
GPIO.setup(15,GPIO.OUT)#Servo 3 Bot
r=GPIO.PWM(11,50)#1
d=GPIO.PWM(13,50)#2
l=GPIO.PWM(15,50)#3
r.start(7.5)#init all three
d.start(7.5)
l.start(7.5)
cur=cur1=cur2=7.5
#time.sleep(1)
f = open("seqin.txt","r")
strin=f.read()#The string
strl=strin.split()#Converted to List
str2=strl[::-1]#Reversed the List

#Going through the list
while(len(str2)):
    if(str2[0]=="R"):
       if(cur!=7.5):
            #open gripper
            r.ChangeDutyCycle(7.5)
            cur=7.5
            #close gripper
       clk(r)
       cur+=5
    if(str2[0]=="Rp"):
         if(cur!=7.5):
            r.ChangeDutyCycle(7.5)
            cur=7.5 
        aclk(r)
        cur-=5
    if(str2[0]=="L"):
        if(cur!=7.5):
            l.ChangeDutyCycle(7.5)
            cur=7.5 
        clk(l)
        cur+=5
    if(str2[0]=="Lp"):
        if(cur!=7.5):
            l.ChangeDutyCycle(7.5)
            cur=7.5 
        aclk(l)
        cur-=5
    if(str2[0]=="D"):
        if(cur!=7.5):
            d.ChangeDutyCycle(7.5)
            cur=7.5 
        clk(d)
        cur+=5
    if(str2[0]=="Dp"):
        if(cur!=7.5):
            d.ChangeDutyCycle(7.5)
            cur=7.5 
        aclk(d)
        cur-=5
    str2.pop()
GPIO.cleanup()

