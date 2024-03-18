import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
dac = []
GPIO.setup(12, GPIO.OUT)
def tobin(n):
    a = list(bin(n))[2:]
    a = [0 for _ in range(8-len(a))] + list(map(int, a))
    print(round(3.3/256*n, 3))
    return a
p = GPIO.PWM(12, 1000)  # channel=12 frequency=50Hz
p.start(0)
try:
    while 1:
        n = int(input())
        p.ChangeDutyCycle(n)
        print((n*3.3/100))
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()