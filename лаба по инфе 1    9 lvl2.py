#вкладчик положил в банк 10000 рублей под 8% в месяц. Определить через какое время сумма удвоится.
x=10000
i=0
while x < 20000:
    i+=1
    x=x*1.08
print(i)
