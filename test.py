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

GPIO.setup(15,GPIO.OUT)#Servo 3 Bot
GPIO.setup(10,GPIO.OUT)#in_1 DC
GPIO.setup(12,GPIO.OUT)#in_2 DC
l=GPIO.PWM(15,50)#3
print "7.5"
l.start(7.5)
x=input()
l.ChangeDutyCycle(7.5)
time.sleep(2)
x=input()
GPIO.output(10,GPIO.HIGH)
GPIO.output(12,GPIO.LOW)
time.sleep(0.75)
GPIO.output(10,GPIO.LOW)
GPIO.output(12,GPIO.LOW)
x=input()
print "12.5"
l.ChangeDutyCycle(12.5)
time.sleep(2)
x=input()
GPIO.output(10,GPIO.LOW)
GPIO.output(12,GPIO.HIGH)
time.sleep(0.5)
GPIO.cleanup()
