# 35 Определить, присутствует ли в заданном массиве, некоторое число

from random import randint 
l = [randint(0,20) for i in range(12)]
print(l)
print (2 in l)

for i in range(12):
    if l[i]==2: print (l[i])
