# 32 Задать массив из 8 элементов, заполненных нулями и единицами вывести их на экран

from random import randint 
l = [randint(0,1) for i in range(8)]
print(l)