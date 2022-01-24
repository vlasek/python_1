# 33 Задать массив из 12 элементов, заполненных числами из [0,9]. Найти сумму положительных/отрицательных элементов массива

from random import randint 
l = [randint(0,10) for i in range(12)]
print(l)
chet=0
nechet=0
for i in range(12):
    if l[i]%2: nechet=nechet+l[i]
    else: chet=chet+l[i]
print('сумма нечетных ', nechet)
print('сумма четных ', chet)

