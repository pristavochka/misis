# В двух заданных одномерных массивах расположить отрицательные элементы в порядке убывания (оставив положительные элементы на прежних местах). 
# Упорядочение отрицательных элементов массива оформить в виде метода.
A=[-34, -54, 68, 12, 33, 51, 1]
B=[49, -58, 97, -83, -30, 99, -51]
def finder(b, a):
    n=[]
    for i in a + b:
        if i < 0:
            n.append(i)
    n.sort(reverse=True)
    index=0
    a1=[]
    b1=[]
    for i in a:
        if i > 0:
            a1.append(i)
        else:
            a1.append(n[index])
            index+=1
    for i in b:
        if i > 0:
            b1.append(i)
        else:
            b1.append(n[index])
            index+=1
    return(a1, b1)
print (finder(A, B))


            
