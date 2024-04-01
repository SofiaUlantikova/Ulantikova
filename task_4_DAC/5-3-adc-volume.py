import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
dac = []
comp = 0
troyka = 0
leds = []
t = 0.001

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(comp, GPIO.IN)
GPIO.setup(troyka, GPIO.OUT, initial=1)
GPIO.setup(leds, GPIO.OUT)
def tobin(n):
    a = list(bin(n))[2:]
    a = [0 for _ in range(8-len(a))] + list(map(int, a))
    print(round(3.3/256*n, 3))
    return a

def adc(t):
    result = 0
    for i in range(8):
        k = 2**(7-i)
        GPIO.output(dac, tobin(result+k))
        time.sleep(t)
        if GPIO.input(comp) == 1:
            result += k
    return result

try:
    while 1:
        val = adc(t)
        print(f'value = {val}, voltage = {3.3*val/256}')
        GPIO.output(leds, tobin(val))
finally:
    GPIO.output(dac, 0)
    GPIO.output(troyka, 0)
    GPIO.output(leds, 0)
    GPIO.cleanup()