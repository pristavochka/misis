c = [1, 2, 3, 4, 4, 4, 3, 4, 2, 4]
c1=[]
m=float('-inf')
for i in range(len(c)):
    if c[i] > m:
        m = c[i]
        c1 = [i]
    elif c[i] == m:
        c1.append(i)
print(c1)