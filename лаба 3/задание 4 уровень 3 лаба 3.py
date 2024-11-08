from random import *
n= int(input())
B=[]
a=[]
r=0
for i in range(0, n-1):
    B.append(randint(1, 50))
print(B)
for i in range(0, n-1):
    if B[i]==max(B):
        if i==0:
            a[i]=0
        elif i==1:
            a[i]=a[0]
        else:
            for x in range(1, i+1):
                r+=B[x-1]
            a.append(r)
    else:
        a.append(B[i])
print(a)
