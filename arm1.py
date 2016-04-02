#code from inter.py copied.
import RPi.GPIO as GPIO
import time
#clk is the function for clockwise rotation of servo
#aclk is for anti-clockwise rotation.Obviously.
def clk(x,cur):
    if(cur!=12.5):
        x.ChangeDutyCycle(cur+5)
        cur+=5
    else:
        v(x)
        x.ChangeDutyCycle(12.5)
    return cur
def aclk(x,cur):
    if(cur!=2.5):
        x.ChangeDutyCycle(cur-5)
        cur-=5
    else:
       	v(x)
        x.ChangeDutyCycle(2.5)
    return cur
def v(x):
    #open gripper
    x.ChangeDutyCycle(7.5)
    #close gripper
    return 7.5
def h(x):
    #open gripper
    x.ChangeDutyCycle(2.5)
    #close gripper
    return 2.5
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
       if(cur1!=7.5):
            cur1=v(d)
       cur=clk(r,cur)
    if(str2[0]=="Rp"):
         if(cur1!=7.5):
            cur1=v(d) 
        cur=aclk(r,cur)
    if(str2[0]=="L"):
       if(cur1!=7.5):
            cur1=v(d)
       cur=clk(l,cur)
    if(str2[0]=="Lp"):
         if(cur1!=7.5):
            cur1=v(d) 
        cur=aclk(l,cur)
    if(str2[0]=="D"):
        if(cur==7.5):
            cur=h(r)
        if(cur2==7.5):
        	cur2=h(l)
        cur1=clk(d)
    if(str2[0]=="Dp"):
        if(cur==7.5):
            cur=h(r)
        if(cur2==7.5):
        	cur2=h(l)
        cur1=aclk(d)
    if(str2[0]=="U"):
    	cur1=v(d)
    	if(cur==2.5):
    		cur=v(r)
    	if(cur2==2.5):
    		cur2=v(l):
    	#open gripper d
    	###run commands simultaneously?
        cur=aclk(r,cur)
        cur2=clk(l,cur)
        #open gripper r and l
        #clode gripper d
        clk(d)
        #close gripper r and l

    str2.pop()
GPIO.cleanup()

