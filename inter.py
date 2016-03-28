'''
duty1=2.5
duty2=7.5
ck=0
while ck<=5:
    pwm.ChangeDutyCycle(duty1)
    pwm2.ChangeDutyCycle(duty1)
    pwm3.ChangeDutyCycle(duty1)
    time.sleep(0.8)
    pwm.ChangeDutyCycle(duty2)
    pwm2.ChangeDutyCycle(duty2)
    pwm2.ChangeDutyCycle(duty2)
    time.sleep(0.8)
    ck=ck+1
time.sleep(1)
'''