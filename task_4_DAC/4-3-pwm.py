import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
port = 24

GPIO.setup(port, GPIO.OUT)

p = GPIO.PWM(port, 1000)  
p.start(0)
try:
    while 1:
        n = float(input())
        p.ChangeDutyCycle(n)
        print(f'voltage: {round(n*3.3/100, 3)}')

finally:
    GPIO.output(port, 0)
    GPIO.cleanup()