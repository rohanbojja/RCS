import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(36,GPIO.OUT)
GPIO.setup(38,GPIO.OUT)
GPIO.setup(40,GPIO.OUT)
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
z=4
y=0.005
while(z>0):
    a=input("s2:")
    b=input("s1:")
    c=input("s0:")
    f(a,b,c)    
    n=input("*")
    z-=1
