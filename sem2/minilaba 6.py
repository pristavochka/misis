from math import sin, cos

x = 3

speed = 0.01

epochs = 100


def difffunc(x):
    y = 2*x
    return y


def func(x):
    y = x**2
    return y


def gradiendDescend(x, speed, epochs):
    xList = []
    yList = []
    for i in range(1, epochs):
        x = x - speed * difffunc(x)
        xList.append(x)
        yList.append(func(x))
    return xList, yList


data = gradiendDescend(x, speed, epochs)

import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

x_vals = np.linspace(0, 10, 100)
ax.plot(x_vals, func(x_vals), label='Функция y = x²')


sizes = np.random.uniform(15, 80, len(data[0]))
colors = np.random.uniform(15, 80, len(data[0]))

scatter = ax.scatter(data[0], data[1], s=sizes, c=colors, 
                    vmin=0, vmax=100, label='Градиентный спуск')

ax.set(xlim=(0, 8), xticks=np.arange(0, 10),
       ylim=(0, 8), yticks=np.arange(0, 10),
       xlabel='x', ylabel='y')
ax.legend()

plt.show()
