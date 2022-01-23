# 31 Задать массив из 8 элементов и вывести их на экран

# list=[8]
# print (list[0])
# import random
# for i in range(8):
#     list[i]=random.randint(0, 10)
#     print (list[i])

from random import randint 
l = [randint(1,100) for i in range(8)]
print(l)
    