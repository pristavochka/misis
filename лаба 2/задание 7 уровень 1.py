x=float(input("введите значение аргумента"))
y=0
if x > 1 or x < -1:
    y=1
else:
    if x>0:
        y=x
    else:
        y=-x
print(y)