import matplotlib.pyplot as plt
import numpy as np

plt.style.use('_mpl-gallery')

# make data
a = 3
b = 2
c = 1
x = np.linspace(0, 20, 50);
y= a * np.cos(x) + b * np.sin(c * x)

# plot
fig, ax = plt.subplots()


ax.plot(x, y, linewidth=2.0)


ax.set(xlim=(-8, 8), xticks=np.arange(-9, 8),
       ylim=(-8, 8), yticks=np.arange(-9, 8))

plt.show()

