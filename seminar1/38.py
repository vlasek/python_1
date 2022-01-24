# 38 Найти сумму чисел одномерного массива стоящих на нечетной позиции


from random import randint 
l = [randint(0,200) for i in range(20)]
print(l)
sum=0

for i in range(20):
    if i%2:
        sum=sum+l[i]
        print (l[i])
   
print('сумма - ', sum)