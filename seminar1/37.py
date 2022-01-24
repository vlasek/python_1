# 37 В одномерном массиве из 123 чисел найти количество элементов из отрезка [10,99]


from random import randint 
l = [randint(0,200) for i in range(123)]
print(l)
count=0

for i in range(123):
    if 10<l[i]<100: 
        # print (l[i])
        count+=1
   
print('кол-во от 10 до 99 - ', count)
