import RPi.GPIO as GPIO
import time
GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8,GPIO.OUT)#IN 1 
GPIO.setup(10,GPIO.OUT)#IN 2 
GPIO.setup(11,GPIO.OUT)#IN 3 
GPIO.setup(12,GPIO.OUT)#IN 4
GPIO.setup(36,GPIO.OUT)
GPIO.setup(38,GPIO.OUT)
GPIO.setup(40,GPIO.OUT)
def s(a,b,c,d):
    if a:
        GPIO.output(8,GPIO.HIGH)
    else :
        GPIO.output(8,GPIO.LOW)
    if b:
        GPIO.output(10,GPIO.HIGH)
    else :
        GPIO.output(10,GPIO.LOW)
    if c:
        GPIO.output(11,GPIO.HIGH)
    else :
        GPIO.output(11,GPIO.LOW)
    if d:
        GPIO.output(12,GPIO.HIGH)
    else :
        GPIO.output(12,GPIO.LOW)
def f(a,b,c):
    if a:
        GPIO.output(36,GPIO.HIGH)
    else :
        GPIO.output(36,GPIO.LOW)
    if b:
        GPIO.output(38,GPIO.HIGH)
    else :
        GPIO.output(38,GPIO.LOW)
    if c:
        GPIO.output(40,GPIO.HIGH)
    else :
        GPIO.output(40,GPIO.LOW)

try:
	z=4
	y=0.005
	Seq = []
        Seq = range(0, 8)
        Seq[0] = [1,0,0,0]
        Seq[1] = [1,0,1,0]
        Seq[2] = [0,0,1,0]
        Seq[3] = [0,1,1,1]
        Seq[4] = [0,1,0,0]
        Seq[5] = [0,1,0,1]
        Seq[6] = [0,0,0,1]
        Seq[7] = [1,0,0,1]
        demux = []
        demux =range(0,8)
        demux[0]=[0,0,0]
        demux[1]=[0,0,1]
        demux[2]=[0,1,0]
        demux[3]=[0,1,1]
        demux[4]=[1,0,0]
        demux[5]=[1,0,1]
        demux[6]=[1,1,0]
        demux[7]=[1,1,1]
        z=0
	while(z<4):
            '''a=input("s2:")
            b=input("s1:")
            c=input("s0:")'''
            f(demux[z][0],demux[z][1],demux[z][2])
            i=0
            x=5
            while(x>0):
                i=0
                temp=0
                while i<temp+8:
                    s(Seq[i%8][0],Seq[i%8][1],Seq[i%8][2],Seq[i%8][3])
                    time.sleep(y)
                    i+=1
                x=x-1
            n=input("*")
            time.sleep(1)
            z+=1
except SyntaxError,KeyboardInterrupt:
	GPIO.cleanup()
GPIO.cleanup()
