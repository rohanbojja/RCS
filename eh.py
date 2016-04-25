import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8,GPIO.OUT)#IN 1 
GPIO.setup(10,GPIO.OUT)#IN 2 
GPIO.setup(11,GPIO.OUT)#IN 3 
GPIO.setup(12,GPIO.OUT)#IN 4
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

try:
	y=0.005
	Seq = []
        Seq = range(0, 8)
        Seq[0] = [1,0,0,0]
        Seq[1] = [1,0,1,0]
        Seq[2] = [0,0,1,0]
        Seq[3] = [0,1,1,0]
        Seq[4] = [0,1,0,0]
        Seq[5] = [0,1,0,1]
        Seq[6] = [0,0,0,1]
        Seq[7] = [1,0,0,1]
        t=0
        i=0
        while t<4:
            x=6
            while(x>0):
                    temp=i
                    while i<temp+8:
                        s(Seq[i%8][0],Seq[i%8][1],Seq[i%8][2],Seq[i%8][3])
                        time.sleep(y)
                        i+=1
                    x=x-1
            temp=i
            while i<4+temp:
                        s(Seq[i%8][0],Seq[i%8][1],Seq[i%8][2],Seq[i%8][3])
                        time.sleep(y)
                        i+=1
            time.sleep(1)
            t+=1
except SyntaxError,KeyboardInterrupt:
	GPIO.cleanup()

GPIO.cleanup()
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8,GPIO.OUT)#IN 1 
GPIO.setup(10,GPIO.OUT)#IN 2 
GPIO.setup(11,GPIO.OUT)#IN 3 
GPIO.setup(12,GPIO.OUT)#IN 4
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

try:
	y=0.005
	Seq = []
        Seq = range(0, 8)
        Seq[0] = [1,0,0,0]
        Seq[1] = [1,0,1,0]
        Seq[2] = [0,0,1,0]
        Seq[3] = [0,1,1,0]
        Seq[4] = [0,1,0,0]
        Seq[5] = [0,1,0,1]
        Seq[6] = [0,0,0,1]
        Seq[7] = [1,0,0,1]
        t=0
        i=0
        while t<4:
            x=6
            while(x>0):
                    temp=i
                    while i<temp+8:
                        s(Seq[i%8][0],Seq[i%8][1],Seq[i%8][2],Seq[i%8][3])
                        time.sleep(y)
                        i+=1
                    x=x-1
            temp=i
            while i<4+temp:
                        s(Seq[i%8][0],Seq[i%8][1],Seq[i%8][2],Seq[i%8][3])
                        time.sleep(y)
                        i+=1
            time.sleep(1)
            t+=1
except SyntaxError,KeyboardInterrupt:
	GPIO.cleanup()

GPIO.cleanup()
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8,GPIO.OUT)#IN 1 
GPIO.setup(10,GPIO.OUT)#IN 2 
GPIO.setup(11,GPIO.OUT)#IN 3 
GPIO.setup(12,GPIO.OUT)#IN 4
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

try:
	y=0.005
	Seq = []
        Seq = range(0, 8)
        Seq[0] = [1,0,0,0]
        Seq[1] = [1,0,1,0]
        Seq[2] = [0,0,1,0]
        Seq[3] = [0,1,1,0]
        Seq[4] = [0,1,0,0]
        Seq[5] = [0,1,0,1]
        Seq[6] = [0,0,0,1]
        Seq[7] = [1,0,0,1]
        t=0
        i=0
        while t<4:
            x=6
            while(x>0):
                    temp=i
                    while i<temp+8:
                        s(Seq[i%8][0],Seq[i%8][1],Seq[i%8][2],Seq[i%8][3])
                        time.sleep(y)
                        i+=1
                    x=x-1
            temp=i
            while i<4+temp:
                        s(Seq[i%8][0],Seq[i%8][1],Seq[i%8][2],Seq[i%8][3])
                        time.sleep(y)
                        i+=1
            time.sleep(1)
            t+=1
except SyntaxError,KeyboardInterrupt:
	GPIO.cleanup()

GPIO.cleanup()
