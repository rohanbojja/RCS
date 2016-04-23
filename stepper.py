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
	y=0.1
	z=6
	x=5
	while(z>0):
            a=input("s2:")
            b=input("s1:")
            c=input("s0:")
            #x=input("duration:")
            f(a,b,c)
            x=25
            while(x>0):
                s(1,0,1,0)
                time.sleep(y)
                s(0,1,1,0)
                time.sleep(y)
                s(0,1,0,1)
                time.sleep(y)
                s(1,0,0,1)
                time.sleep(y) 
                x=x-1
            z-=1
except SyntaxError,KeyboardInterrupt:
	GPIO.cleanup()

GPIO.cleanup()
