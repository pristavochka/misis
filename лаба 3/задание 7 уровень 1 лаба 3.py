a= [2, 6, 18, 31, 7, 10, 5]
i=0
x=0
for i in range(0, 6):
    x=x+a[i]
x=x/7
for i in range(0, 6):
    if a[i]>x:
        a[i]=0
print(a, x)