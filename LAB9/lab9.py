#Если максимальный элемент массива больше суммы элементов массива, заменить его нулем, иначе - удвоить.
f = open(r"c:\Users\m2406454\Desktop\LAB9\arrayin.txt", 'r')
e = f.read()
a = e.split(' ')
c=0
for b in range(len(a)):
    a[b] = int(a[b])
    c += a[b]
for i in range(len(a)):
    if a[i] == max(a):
        if a[i] > c:
            a[i]=0
        else:
            a[i]=2*a[i]
f = open(r"c:\Users\m2406454\Desktop\LAB9\arrayout.txt", 'w')
for i in a:
    i=str(i)
    f.write(i + ' ')
print(a)


