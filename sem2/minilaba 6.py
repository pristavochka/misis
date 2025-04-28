from math import e 
x=3

speed = 0.00001

epochs = 100

def difffunc(x):
    y = 2*x*e**(x**2)+2*x 
    return y
def func(x):
    y = e**(x**2) + x**2
    return y 
def gradiendDescend(x, speed, epochs):
    xList=[]
    yList=[]
    for i in range(1, epochs):
        x = x - speed * difffunc(x) 
        xList.append(x)
        yList.append(func(x))
    return xList, yList
data = gradiendDescend(x, speed, epochs)


import matplotlib.pyplot as plt
import numpy as np
 
fig, ax = plt.subplots()
x = np.linespace(0,10,100)
ax.plot(x, func(x))
plt.show()
sizes = np.random.uniform(15, 80, len(x))
colors = np.random.uniform(15, 80, len(x))
fig, ax = plt.subplots()

ax.scatter(data[0], data[1], s=sizes, c=colors, vmin=0, vmax=100)

ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
       ylim=(0, 8), yticks=np.arange(1, 8))

plt.show()