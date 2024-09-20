import math
h=0
s=1000
i=0
for x in range(1, 10 , 1):
    if s < 0.0001:
        print(round(h,4))
        break
    else:
        s=((-1)**i)*((x/10)**2*i)/math.factorial(2*i)
        h+=s
        i+=1
    print(math.cos(x/10))
