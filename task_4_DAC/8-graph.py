import matplotlib.pyplot as plt
import numpy as np
from math import ceil

with open('settings.txt', 'r') as f:
    data = [float(line) for line in f.read().split('\n')]

freq = data[0]

period = 1/freq

step = data[1]

voltage = np.loadtxt('data.txt', dtype=float)

voltage *= 3.3/256

timepoints = np.linspace(0, len(voltage)*period, len(voltage))

ind_max = np.argmax(voltage)

time_charged = timepoints[ind_max]

time_discharged = timepoints[-1] - time_charged

fig, ax = plt.subplots()

ax.plot(timepoints, voltage, 'b', label='V(t)')

ax.scatter(timepoints[::round(freq)], voltage[::round(freq)], color='b', marker='o', linewidths=2)

plt.xticks(np.arange(0, ceil(len(voltage)*period)))

plt.xlim(-len(voltage)*period*0.05, ceil(len(voltage)*period))

plt.ylim(0, 1.1*np.max(voltage))

plt.xlabel('Time, s')

plt.ylabel('Voltage, V')

plt.grid(which='major', color='g', linewidth=1.5, alpha=0.5)

plt.grid(which='minor', color='g', linestyle='--', linewidth=1, alpha=0.2)

ax.minorticks_on()

plt.legend(loc=1)

plt.title(label='Процесс заряда и разряда конденсатора в RC-цепи', loc='center', wrap=True)

plt.text(0.55*timepoints[-1], 0.8*np.max(voltage), f'Время зарядки = {time_charged:4.1f} с', wrap=True)

plt.text(0.6*timepoints[-1], 0.65*np.max(voltage), f'Время разрядки = {time_discharged:4.1f} с', wrap=True)

plt.show()