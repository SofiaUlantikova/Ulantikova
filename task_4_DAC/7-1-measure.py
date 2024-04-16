import time
import RPi.GPIO as GPIO
import matplotlib.pyplot as plt
import numpy as np
GPIO.setmode(GPIO.BCM)
dac = [8, 11, 7, 1, 0, 5, 12, 6]
comp = 14
troyka = 13
leds = [2, 3, 4, 17, 27, 22, 10, 9]
period = 0.005 # for measure() function

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(comp, GPIO.IN)
GPIO.setup(troyka, GPIO.OUT, initial=0)
GPIO.setup(leds, GPIO.OUT)
def tobin(n):
    a = list(bin(n))[2:]
    a = [0 for _ in range(8-len(a))] + list(map(int, a))
    return a

def measure(t): # t - period of waiting for RPi to change output on DAC before measuring
    result = 0
    for i in range(8): # binary search realization
        k = 2**(7-i)
        GPIO.output(dac, tobin(result+k))
        time.sleep(t)
        if GPIO.input(comp) == 0: # if troyka voltage more than DAC
            result += k
    return result

def show(val):
    a = (val + 1) // 32
    '''from 8-digit to 3-digit, if voltage from 32k to 32k+31 -- k leds enlightened 
    (8 leds if only max_voltage (256) found)'''
    GPIO.output(leds, [0 for _ in range(8 - a)] + [1 for _ in range(a)])

def binary_to_volts(val):
    return 3.3*val/256

try:
    data = []
    t0 = time.time()
    GPIO.output(troyka, 1)
    v = measure(period) # binary representation of voltage
    while v < 249: # max voltage in binary representation is 256, 97 % of max voltage = 248.3
        data.append(binary_to_volts(v))
        v = measure(period)
    GPIO.output(troyka, 0)
    while v > 5: # 2 % of max voltage = 5.1
        data.append(binary_to_volts(v))
        v = measure(period)
    data.append(binary_to_volts(v))
    t1 = time.time()
    span = t1 - t0 # duration of experiment
    fig, ax = plt.subplots()
    moments = np.linspace(0, span, len(data)) # timepoints of measurements
    ax.plot(moments, data)
    plt.xlabel('Time, s')
    plt.ylabel('Voltage, V')
    plt.grid()
    plt.show()
    with open('data.txt', 'w') as file:
        data_strs = '\n'.join(data)
        file.write(data.strs)
    measure_period = span / len(data)
    frequency = 1 / measure_period
    step_discret = 3.3/256
    with open('settings.txt', 'w') as file:
        file.write(f'Средняя частота диксретизации = {frequency} Гц\nШаг квантования = {step_discret} В')
    print(f'Общая продолжительность эксперимента = {span} с\nПериод одного измерения = {measure_period} с \nСредняя частота дискретизации = {frequency} Гц \nШаг квантования АЦП = {step_discret} В')

finally:
    GPIO.output(dac, 0)
    GPIO.output(troyka, 0)
    GPIO.output(leds, 0)
    GPIO.cleanup()