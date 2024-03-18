import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
dac = []
GPIO.setup(dac, GPIO.OUT)
def tobin(n):
    a = list(bin(n))[2:]
    a = [0 for _ in range(8-len(a))] + list(map(int, a))
    print(round(3.3/256*n, 3))
    return a
period = float(input())
dt = period/(255+256)
try:
    while 1:
        for i in range(256):
            GPIO.output(dac, tobin(i))
            time.sleep(dt)
        for i in range(255, 0, -1):
            GPIO.output(dac, tobin(i))
            time.sleep(dt)
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()