from random import *
n= int(input())
B=[]
a=[]
for i in range(0, n-1):
    B.append(randint(1, 50))
print(B)
for i in range(0, n-1):
    a.append(B[i])
    if B[i]==max(B):
        if i==0:
            a[i]=0
        else:
            for x in range(1, i):
                a[i]+=B[x-1]
print(a)