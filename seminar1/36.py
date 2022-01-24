# 36 Задать массив, заполнить случайными положительными трёхзначными числами. Показать количество нечетных\четных чисел

from random import randint 
l = [randint(100,1000) for i in range(12)]
print(l)
chet=0
nechet=0
for i in range(12):
    if l[i]%2: nechet+=1
    else: chet+=1
print('кол-во нечетных ', nechet)
print('кол-во четных ', chet)