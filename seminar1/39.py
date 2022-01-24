# 39 Найти произведение пар чисел в одномерном массиве. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

from random import randint 
count=4
l = [randint(1,10) for i in range(count)]
print(l)


for i in range(count//2):
    print (l[i]*l[len(l)-1])
    
   