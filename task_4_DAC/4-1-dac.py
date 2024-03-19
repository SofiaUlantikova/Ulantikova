import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
dac = [8, 11, 7, 1, 0, 5, 12, 6]
GPIO.setup(dac, GPIO.OUT)
def tobin(n):
    a = list(bin(n))[2:]
    a = [0 for _ in range(8-len(a))] + list(map(int, a))
    print(f'Voltage = {round(3.3/256*n, 3)}')
    return a

try:
    while 1:
        c = input('put an integer in range from 0 to 255: ')
        try:
            n = int(c)
            if n < 0:
                print('put positive integer')
                continue
            if n > 255:
                print('put an integer less then 256')
                continue
            GPIO.output(dac, tobin(n))
        except ValueError:
            if c == 'q':
                break
            elif float(c) % 1 > 0:
                print('put an integer, not a float')
                continue
            else:
                print('put an integer, not a symbol')
                continue
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()