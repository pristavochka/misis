n=5
import math
for run in range(1, n):
    A = int(input("Введите парамтер А"))
    B = int(input("Введите парамтер B"))
    x = int(input("для площади прямоугольника введите 1 для площади кольца введите 2 для площади треугольника введите 3"))
    if x == 1:
        print(A*B)
    elif x == 2:
        if A > B:
            print(A*math.pi*A-B*B*math.pi)
        else:
            print(B*math.pi*B-A*A*math.pi)
    elif x == 3:
        print((math.sqrt(B*B-(A/2)*(A/2))*A)/2)