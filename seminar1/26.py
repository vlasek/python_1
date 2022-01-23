# 26 Возведите число А в натуральную степень B используя цикл
# a=2
# b=5
a = int(input('a= '))
b = int(input('b= '))
c = 1
for i in range(1, b+1):
    c = c*a
    # print (c)

print(f'a = {a} в степени b = {b} равно {c}')
