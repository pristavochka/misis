import math
import random
import numpy as np
import matplotlib.pyplot as plt

xMin1, xMax1, yMin1, yMax1 = 0, 50, 0, 50
xMin2, xMax2, yMin2, yMax2 = 25, 75, 25, 75
k = 3
p = 0.8

classesCount = 2
pointsCount1 = 50
pointsCount2 = 50
#создаем список точек и присваеваем им классы 1 и 0
def generator(count, x_min, x_max, y_min, y_max):
    allpoints = []
    for i in range(count):
        x = random.uniform(x_min, x_max)
        y = random.uniform(y_min, y_max)
        allpoints.append([x, y])
    return allpoints

x1 = generator(pointsCount1, xMin1, xMax1, yMin1, yMax1)
x2 = generator(pointsCount2, xMin2, xMax2, yMin2, yMax2)
x = x1 + x2
y = [0] * pointsCount1 + [1] * pointsCount2

#разделяем точки на train и test в соотношении p
def train_test_split(x, y, p):
    x_train = []
    y_train = []
    x_test = []
    y_test = []
    for i in range(round((pointsCount1 + pointsCount2) * p)):
        x_train.append(x[i])
        y_train.append(y[i])
    for l in range(round((pointsCount1 + pointsCount2) * (1 - p))):
        x_test.append(x[l])
        y_test.append(y[l])

    return x_train, x_test, y_train, y_test
x_train, x_test, y_train, y_test = train_test_split(x, y, p)
# применяем метод k ближайших соседей
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
def fit(x_train, y_train, x_test):
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(x_train, y_train)
    y_predict = knn.predict(x_test)
    return y_predict
y_predict1 = fit(x_train, y_train, x_test)
# считаем точность программы если predict совпадает с test то программа отработала точно
sovp=0
for i in range(len(y_predict1)):
    if y_predict1[i]==y_test[i]:
        sovp+=1
accuracy=sovp/len(y_predict1)
print('точность:', accuracy)
#визуеализируем результат
def output(x_train, y_train, x_test, y_test, y_predict1):
    for x, y in zip(x_train, y_train):
        marker = 'o' if y == 0 else 'x'
        plt.plot(x[0], x[1], marker, color='blue')

    for x, ytr, ypred in zip(x_test, y_test, y_predict1):
        color = 'green' if ytr == ypred else 'red'
        marker = 'o' if ytr == 0 else 'x'
        plt.plot(x[0], x[1], marker, color=color)

    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('визуализация результата')
    plt.show()

output(x_train, y_train, x_test, y_test, y_predict1)