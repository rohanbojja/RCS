#MB1
import RPi.GPIO as GPIO
import time
#def clk(x):
#    x.ChangeDutyCycle(12.5)
#def aclk(x):
#    x.ChangeDutyCycle(2.5)
#10,12 DC Motor_1
#16,18 DC motor2
GPIO.setmode(GPIO.BOARD)
#DC MOTOR Bot
GPIO.setup(10,GPIO.OUT)#in_1
GPIO.setup(12,GPIO.OUT)#in_2
#DC MOTOR Left
GPIO.setup(16,GPIO.OUT)#in_3
GPIO.setup(18,GPIO.OUT)#in_4
GPIO.setup(15,GPIO.OUT)#Right Servo
GPIO.setup(13,GPIO.OUT)#Bot Servo
d=GPIO.PWM(13,50)#Bot
r=GPIO.PWM(15,50)#Right
r.start(7.5)
d.start(7.5)
print "config1"
GPIO.output(10,GPIO.HIGH)
GPIO.output(12,GPIO.LOW)
GPIO.output(16,GPIO.HIGH)
GPIO.output(18,GPIO.LOW)
time.sleep(0.5)
#clk(r)
GPIO.output(10,GPIO.LOW)
GPIO.output(12,GPIO.LOW)
GPIO.output(16,GPIO.LOW)
GPIO.output(18,GPIO.LOW)
p=raw_input("Start?")

#input()
print "config 2"
GPIO.output(10,GPIO.LOW)
GPIO.output(12,GPIO.HIGH)
GPIO.output(16,GPIO.LOW)
GPIO.output(18,GPIO.HIGH)
k=raw_input("rotate?")
#aclk(r)
r.ChangeDutyCycle(10.5)
time.sleep(0.75)
GPIO.output(10,GPIO.LOW)
GPIO.output(12,GPIO.LOW)
GPIO.output(16,GPIO.LOW)
GPIO.output(18,GPIO.LOW)
r.ChangeDutyCycle(2.5)

print "closed"
#GPIO.output(8,GPIO.LOW)
GPIO.cleanup()
