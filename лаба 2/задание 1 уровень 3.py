x=int(input("Введите количество девочек"))
y=int(input("Введите количество мальчиков"))
n=0
f=0
for run in range(1, x+1):
    a=int(input("Введите рост девочки"))
    n=n+a
print(n/x)
for run in range(1, y+1):
    b=int(input("Введите рост мальчика"))
    f=f+b
print(f/y)
