A=[[1, 25, 44, 31, 7],[4, 31, 9, 71, 56],[6, 45, 82, 70, 33],[4, 87, 36, 28, 9],[20, 49, 51, 26, 65]]
b=[]
for i in range(0, 5):
    b.append(A[i][i])
for k in range(0, 5):
    if b[k]==max(b):
        A.append(A[k])
        A[k]=A[3]
        A[3]=A[5]
        A=A[:5]
print(A)
