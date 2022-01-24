# 34 Написать программу замену элементов массива на противоположные
from random import randint 
l = [randint(-10,10) for i in range(12)]
print(l)

for i in range (12):
    if l[i]<0: l[i]=-l[i]
    else: l[i]=-l[i]
print (l)