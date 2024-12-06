#В массив В размером 4 × 5 вставить после строки, содержащей максимальное количество положительных элементов, столбец массива С размером 5 × 6, содержащий максимальное количество положительных элементов. Определение количества положительных элементов в заданной строке (или столбце) матрицы осуществить в методе.
def counter(array):
    count = 0
    for element in array:
        if element > 0:
            count += 1
    return count
def finder(B):
    row = -1
    max_count = -1
    for i in range(len(B)):
        count = counter(B[i])
        if count > max_count:
            max_count = count
            row = i
    return row
def finder_but_for_cols(o):
    col = -1
    max_count = -1
    a = len(o)
    b = len(o[0]) if a > 0 else 0    
    for j in range(b):
        cl = [o[i][j] for i in range(a)]
        count = counter(cl)
        if count > max_count:
            max_count = count
            col = j
    return col
B = [
    [1, -2, 0, 4, -5],
    [7, 8, -9, 0, 2],
    [-1, -1, -1, 1, 1],
    [2, 2, -6, -7, 8]
]
C = [
    [1, 2, -3, 4, 5, -6],
    [-1, -2, 3, 4, -5, 6],
    [7, -8, -9, 0, 1, 2],
    [-1, 1, 1, -1, 1, 1],
    [2, 2, 2, 2, 2, 2]
]
d = finder(B)
e = finder_but_for_cols(C)
if d != -1 and e != -1:
    B.insert(d + 1, [C[i][e] for i in range(len(C))])
for f in B:
    print(f)