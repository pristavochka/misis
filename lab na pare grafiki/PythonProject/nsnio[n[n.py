import matplotlib.pyplot as plt
import numpy as np


# make data
file = open("input.txt","r")
s = file.readlines()
print(s)
x = list(map(float,s[0][:-1].split(",")))
y = list(map(float,s[1].split(",")))
# plot
fig, ax = plt.subplots()


ax.plot(x, y, linewidth=2.0)

plt.show()