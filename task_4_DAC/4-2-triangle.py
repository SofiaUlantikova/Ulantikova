import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
dac = [8, 11, 7, 1, 0, 5, 12, 6]
GPIO.setup(dac, GPIO.OUT)
def tobin(n):
    a = list(bin(n))[2:]
    a = [0 for _ in range(8-len(a))] + list(map(int, a))
    return a
period = float(input())
dt = period/(255+256)
try:
    while 1:
        for i in range(256):
            GPIO.output(dac, tobin(i))
            time.sleep(dt)
        for i in range(254, 0, -1):
            GPIO.output(dac, tobin(i))
            time.sleep(dt)
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()