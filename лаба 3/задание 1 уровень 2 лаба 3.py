#Минимальный элемент заданного одномерного массива увеличить в 2 раза.
from random import *
n= int(input())
a=[]
b=[]
for i in range(0, n-1):
    a.append(randint(1, 50))
print(a)
for i in range(0, n-1):
    b.append(a[i])
    if a[i]==min(a):
        b[i]=2*a[i]
print(b)
