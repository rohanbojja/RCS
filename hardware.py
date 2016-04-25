import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(8,GPIO.OUT)#Stepper Motor    IN 1
GPIO.setup(16,GPIO.OUT)#Stepper Motor   IN 2
GPIO.setup(11,GPIO.OUT)#Stepper Motor   IN 3
GPIO.setup(12,GPIO.OUT)#Stepper Motor   IN 4
GPIO.setup(36,GPIO.OUT)#DeMux selector  S0
GPIO.setup(38,GPIO.OUT)#DeMux selector  S1
GPIO.setup(40,GPIO.OUT)#DeMux selector  S2

def sel(a,b,c):
        if a:
                GPIO.output(36,GPIO.HIGH)
        else:
                GPIO.output(36,GPIO.LOW)
        if b:
                GPIO.output(38,GPIO.HIGH)
        else:
                GPIO.output(38,GPIO.LOW)
        if c:
                GPIO.output(40,GPIO.HIGH)
        else:
                GPIO.output(40,GPIO.LOW)

def s(a,c,b,d):
    if a:
        GPIO.output(8,GPIO.HIGH)
    else :
        GPIO.output(8,GPIO.LOW)
    if b:
        GPIO.output(16,GPIO.HIGH)
    else :
        GPIO.output(16,GPIO.LOW)
    if c:
        GPIO.output(11,GPIO.HIGH)
    else :
        GPIO.output(11,GPIO.LOW)
    if d:
        GPIO.output(12,GPIO.HIGH)
    else :
        GPIO.output(12,GPIO.LOW)

def clk(a):
	if(a):
                x=6
                m=2
        else:
                x=12
                m=4
        try:
                y=0.005
                Seq = []
                Seq = range(0, 8)
                Seq[0] = [1,0,0,0]
                Seq[1] = [1,1,0,0]
                Seq[2] = [0,1,0,0]
                Seq[3] = [0,1,1,0]
                Seq[4] = [0,0,1,0]
                Seq[5] = [0,0,1,1]
                Seq[6] = [0,0,0,1]
                Seq[7] = [1,0,0,1]
                i=0    
                while(x>0):
                        temp=i
                        while i<8+temp:
                                print Seq[i%8]
                                s(Seq[i%8][0],Seq[i%8][1],Seq[i%8][2],Seq[i%8][3])
                                time.sleep(y)
                                i+=1
                        x=x-1
                i=0
                temp=i
                while i<m+temp:
                        print Seq[i%8]
                        s(Seq[i%8][0],Seq[i%8][1],Seq[i%8][2],Seq[i%8][3])
                        time.sleep(y)
                        i+=1
        except SyntaxError,KeyboardInterrupt:
                GPIO.cleanup()

def clk(a):
	if(a):
                x=6
                m=2
        else:
                x=12
                m=4
        try:
                y=0.005
                Seq = []
                Seq = range(0, 8)
                Seq[7] = [1,0,0,0]
                Seq[6] = [1,1,0,0]
                Seq[5] = [0,1,0,0]
                Seq[4] = [0,1,1,0]
                Seq[3] = [0,0,1,0]
                Seq[2] = [0,0,1,1]
                Seq[1] = [0,0,0,1]
                Seq[0] = [1,0,0,1]
                i=0    
                while(x>0):
                        temp=i
                        while i<8+temp:
                                print Seq[i%8]
                                s(Seq[i%8][0],Seq[i%8][1],Seq[i%8][2],Seq[i%8][3])
                                time.sleep(y)
                                i+=1
                        x=x-1
                i=0
                temp=i
                while i<m+temp:
                        print Seq[i%8]
                        s(Seq[i%8][0],Seq[i%8][1],Seq[i%8][2],Seq[i%8][3])
                        time.sleep(y)
                        i+=1
        except SyntaxError,KeyboardInterrupt:
                GPIO.cleanup()
                
f = open("seqin.txt","r")
strin=f.read()#The string
strl=strin.split()#Converted to List
str2=strl[::-1]#Reversed the List

#Add selector pins appropriately
while(len(str2)):
	#Functions
	if(str2[0]=="R"):
                sel(0,0,0)
		clk(0)
	elif(str2[0]=="L"):
                sel(0,0,1)
		clk(0)
	elif(str2[0]=="D"):
                sel(0,1,0)
		clk(1)
	elif(str2[0]=="F"):
                sel(0,1,1)
		clk(1)
	elif(str2[0]=="U"):
                sel(1,0,0)
		clk(1)
	elif(str2[0]=="B"):
                sel(1,0,1)
		clk(1)
	#Primes
	elif(str2[0]=="R"):
                sel(0,0,0)
		aclk(0)
	elif(str2[0]=="L"):
                sel(0,0,1)
		aclk(0)
	elif(str2[0]=="D"):
                sel(0,1,0)
		aclk(1)
	elif(str2[0]=="F"):
                sel(0,1,1)
		aclk(1)
	elif(str2[0]=="U"):
                sel(1,0,0)
		aclk(1)
	elif(str2[0]=="B"):
                sel(1,0,1)
		aclk(1)	
	str2.pop()
GPIO.cleanup()
