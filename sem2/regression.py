import matplotlib.pyplot as plt
import random as rnd

import numpy as np

import numpy as np

N = 15
ALPHA = 0.0001

x = np.linspace(0,N,N*2)

y = []
y_real = []



def func(x):
    A = 2
    B = 2
    C = 5
    pt_y = A * (x ** B) + C
    return pt_y

for pt_x in x:
    pt_y = func(pt_x)
    y_real.append(pt_y)
    y.append(pt_y + rnd.uniform(-6,6))


fig, ax = plt.subplots()

ax.plot(x, y_real, c='green')

scatter_objects = []
plot_objects = []

import numpy as np

def gradient_descent(x, y, a_start, b_start, c_start, alpha, max_iterations):
    x = np.where(x <= 0, 1e-10, x)

    n = len(x)
    a, b, c = a_start, b_start, c_start

    for _ in range(max_iterations):
        x_b = x ** b
        y_pred = a * x_b + c


        grad_a = (2 / n) * np.sum((y_pred - y) * x_b)
        grad_b = (2 / n) * np.sum((y_pred - y) * a * x_b * np.log(x))
        grad_c = (2 / n) * np.sum((y_pred - y))

        a -= alpha * grad_a * 1
        b -= alpha * grad_b * 0.01
        c -= alpha * grad_c * 1

    final_y_pred = a * (x ** b) + c
    return final_y_pred.tolist()

def update(MAX_ITER):
    global scatter_objects, plot_objects

    for scatter in scatter_objects:
        scatter.remove()
    scatter_objects.clear()

    for line in plot_objects:
        line.remove()
    plot_objects.clear()

    y_pred = gradient_descent(x,y,1,1,1,ALPHA,MAX_ITER)

    scatters = ax.scatter(x, y, c='blue')
    scatter_objects.append(scatters)

    lines = ax.plot(x, y_pred, c='red')
    plot_objects.extend(lines)

    fig.canvas.draw_idle()

axfreq = fig.add_axes([0.25, 0.01, 0.65, 0.03])

freq_slider = plt.Slider(
    ax=axfreq,
    label='Iterations',
    valmin=0,
    valmax=1000,
    valinit=1,
    valstep=1,
)
freq_slider.on_changed(update)
update(0)
plt.show()