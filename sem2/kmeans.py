import numpy as np
import matplotlib.pyplot as plt
import random

list = [[np.random.randint(1, 10), np.random.randint(1, 10)] for _ in range(30)]
x1, y1 = [p[0] for p in list], [p[1] for p in list]
fig, ax = plt.subplots()
ax.scatter(x1, y1)
plt.show()

k = 3
xc1 = random.randint(1, 10)
yc1 = random.randint(1, 10)
xc2 = random.randint(1, 10)
yc2 = random.randint(1, 10)
xc3 = random.randint(1, 10)
yc3 = random.randint(1, 10)

for i in range(50):
    dist1 = []
    dist2 = []
    dist3 = []
    for i in range(len(x1)):
        dist1.append((((x1[i] - xc1) ** 2 + (y1[i] - yc1) ** 2)) ** 0.5)
        dist2.append((((x1[i] - xc2) ** 2 + (y1[i] - yc2) ** 2)) ** 0.5)
        dist3.append((((x1[i] - xc3) ** 2 + (y1[i] - yc3) ** 2)) ** 0.5)

    metka = []
    for j in range(len(x1)):
        mini_dist = min(dist1[j], dist2[j], dist3[j])
        if mini_dist == dist1[j]:
            metka.append(1)
        elif mini_dist == dist2[j]:
            metka.append(2)
        else:
            metka.append(3)

    nclass1 = metka.count(1)
    nclass2 = metka.count(2)
    nclass3 = metka.count(3)

    sredx1, sredy1, sredx2, sredy2, sredx3, sredy3 = 0, 0, 0, 0, 0, 0
    for m in range(len(x1)):
        if metka[m] == 1:
            sredx1 += x1[m]
            sredy1 += y1[m]
        elif metka[m] == 2:
            sredx2 += x1[m]
            sredy2 += y1[m]
        else:
            sredx3 += x1[m]
            sredy3 += y1[m]

    sredx1 = sredx1 / nclass1 if nclass1 != 0 else xc1
    sredy1 = sredy1 / nclass1 if nclass1 != 0 else yc1
    sredx2 = sredx2 / nclass2 if nclass2 != 0 else xc2
    sredy2 = sredy2 / nclass2 if nclass2 != 0 else yc2
    sredx3 = sredx3 / nclass3 if nclass3 != 0 else xc3
    sredy3 = sredy3 / nclass3 if nclass3 != 0 else yc3
    cn1 = [sredx1, sredy1]
    cn2 = [sredx2, sredy2]
    cn3 = [sredx3, sredy3]

    xc1, yc1 = sredx1, sredy1
    xc2, yc2 = sredx2, sredy2
    xc3, yc3 = sredx3, sredy3

fig, ax = plt.subplots()
colors = ['red' if m == 1 else 'green' if m == 2 else 'yellow' for m in metka]
ax.scatter(x1, y1, c=colors)
ax.scatter([xc1], [yc1], marker='x', s=200, c='red')
ax.scatter([xc2], [yc2], marker='x', s=200, c='green')
ax.scatter([xc3], [yc3], marker='x', s=200, c='yellow')

plt.show()

print("centers", cn1, cn2, cn3)
print("type", metka)