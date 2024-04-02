import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
dac = [8, 11, 7, 1, 0, 5, 12, 6]
comp = 14
troyka = 13
t = 0.005

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(comp, GPIO.IN)
GPIO.setup(troyka, GPIO.OUT, initial=1)
def tobin(n):
    a = list(bin(n))[2:]
    a = [0 for _ in range(8-len(a))] + list(map(int, a))
    return a

def adc(t):
    for i in range(256):
        GPIO.output(dac, tobin(i))
        time.sleep(t)
        if GPIO.input(comp) == 1:
            return i

try:
    while 1:
        val = adc(t)
        print(f'value = {val}, voltage = {3.3*val/256}')
finally:
    GPIO.output(dac, 0)
    GPIO.output(troyka, 0)
    GPIO.cleanup()