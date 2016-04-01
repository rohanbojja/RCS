import RPi.GPIO as GPIO
import time
#8,10,12 DC Motor_1
GPIO.setmode(GPIO.BOARD)
#GPIO.setup(8,GPIO.OUT)#Enable
GPIO.setup(10,GPIO.OUT)#in_1
GPIO.setup(12,GPIO.OUT)#in_2
#
#
#
#GPIO.output(8,GPIO.HIGH)#Enabled
GPIO.output(10,GPIO.HIGH)
GPIO.output(12,GPIO.LOW)
time.sleep(0.8)
GPIO.output(10,GPIO.LOW)
GPIO.output(12,GPIO.LOW)
#GPIO.output(8,GPIO.LOW)
GPIO.cleanup()
