A=[[1, 25, 44, 31, 7],
   [4, 31, 9, 71, 56],
   [6, 45, 82, 70, 33],
   [4, 87, 36, 28, 9],
   [20, 49, 51, 26, 65],
   [42, 56, 76, 43, 12],
   [26, 32, 58, 73, 15]]
B=[1, 2, 3, 4, 5]
c=[]
for i in range (0, 5):
    for k in range(0, 7):
        c.append(A[k][i])
    for l in range(0, 7):
        if c[l]==max(c):
            A[l][i]=B[i]
    c=[]
print (A)