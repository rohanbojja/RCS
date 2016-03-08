import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
pwm=GPIO.PWM(11,50)
pwm2=GPIO.PWM(15,50)
pwm.start(5)
pwm2.start(5)
duty1=2.5

duty2=12.5

ck=0
while ck<=5:
    pwm.ChangeDutyCycle(duty1)
    pwm2.ChangeDutyCycle(duty1)
    time.sleep(0.8)
    pwm.ChangeDutyCycle(duty2)
    pwm2.ChangeDutyCycle(duty2)
    time.sleep(0.8)
    ck=ck+1
time.sleep(1)
#Interprets the moves in "seqin.txt" in this directory.
f = open("seqin.txt","r")
strin=f.read()#The string
strl=strin.split()#Converted to List
str2=strl[::-1]#Reversed the List
print str2

#Going through the list
while(len(str2)):
	print str2[len(str2)-1]#REPLACE THIS WITH THE ACTUAL THING, Hardware Interaction
	str2.pop()
GPIO.cleanup()