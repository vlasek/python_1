# Семинар 3-4: примерный список задач
# 11 Для натурального N создать список: 1, -3, 9, -27, 81 и т.д.

# a=int(input('11 Для натурального N создать список: 1, -3, 9, -27, 81 и т.д.  '))


print ('11 задача ')
def create_array_base_on_three(n):
    return [(-3)**i for i in range(n+1)]

print(create_array_base_on_three(8)) # a=8

# 12 Для натурального N создать словарь индекс-значение, состоящий из элементов последовательности 3k + 1.
def create_dict(n):
    return {i: 3*i + 1 for i in range(1, n)}
print (create_dict)

# 13 Пользователь задаёт две строки. Определить количество количество вхождений одной строки в другой.
str1 = 'abrakadabra bayfbabaraba'
str2 = 'ba'
def counter_in (s1, s2):
    count = 0
    while s2 in s1:
        count+=1
        s1 = s1[s1.find(s2) + 1:] # вместо 1 len(str2) образаю символ
    return count
print(counter_in(str1, str2))

# 14 Подсчитать сумму цифр в вещественном числе.
def sum_of_digit(n):
    sum = 0
    for s in str(n):
        if not (s == '.'): # if s !='.'
            sum += int(s)
            print (s, end=' ')
    return sum
print(sum_of_digit(1.342535))

# 15 Написать программу получающую набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда
# [ 1, 2, 6, 24 ]

def set_of_multiple(n):
    return 1 if n == 1 else set_of_multiple(n-1)*n

def fill_miltiple(n):
    return [set_of_multiple(i) for i in range(1,n+1)]

print(fill_miltiple(8))
# 16 Задать список из n чисел последовательности (1+1n)n и вывести на экран их сумму
def create_list(n):
    return sum([((1 + (1 / i))**i) for i in range(1, n + 1)])

list=[]
for i in range(1, 10 + 1):
    list.append ((1+(1/i))**i)
print (list)
print (create_list(10))

# 17 Задать список из N элементов, заполненных числами из [-N, N]. Найти произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число

from random import randint
n=10
new_array = [randint(-n, n) for i in range(10)]
print (new_array)

# 18 Реализовать алгоритм перемешивания списка. 

from random import randint
from xxlimited import new
print ('19 задача ')
new_array = [i for i in range(10)] # randint(0,20) or i последовательно
print(new_array)

def mixing_list(x):
    for i in range (len(x)-1):
        index = randint(i+1, len(x)-1)
        x[i], x[index] =  x[index], x[i] 
    return x

print(mixing_list(new_array))

# 19 Реализовать алгоритм задания случайных чисел. Без использования встроенного генератора псевдослучайных чисел
import datetime

def get_rand():
    return datetime.datetime.now().microsecond % 100
print (get_rand())

# 20 Определить, присутствует ли в заданном списке строк, некоторое число 
def find_str(n):
    list = ['5', '2', '7', 'hi','18', 'bye']
    for s in list:
        if s == str(n):
            return ('Присутствует')
    return("Строчки нет")
print(find_str('hi'))

# 21 Определить, позицию второго вхождения строки в списке либо сообщить, что его нет.
# 22 Найти сумму чисел списка стоящих на нечетной позиции

from random import randint
print ('22 задача ')
new_array = [randint(0,20) for i in range(10)] 
print(new_array)
def sum_not_even(n): 
    return sum(n[1::2]) 
print(sum_not_even(new_array))
    
# 23 Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д. Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15] 
data=[1,2,5,3]
print(data)
data2=[]
def check_multi(d):
    if not len(data)%2: r=len(data)//2
    else: r=len(data)//2+1
    for i in range(r):
        data2.append(data[i]*data[-1-i])
    return data2

print(check_multi(data))




# 24 В заданном списке вещественных чисел найдите разницу между максимальным и минимальным значением дробной части элементов. Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19
import math
list=[1.1, 1.2, 3.1, 5, 10.01]
print (list)

list2=[]
def task24(n):
    for i in list:
        # print (type(i))
        if type (i) == float:
            list2.append(round(i-int(i),2)) 
    return round((max(list2)-min(list2)),3)

print(task24(list))
# 25 Написать программу преобразования десятичного числа в двоичное
# 25 Написать программу преобразования десятичного числа в двоичное
n=255
list=[]
# 10%2 = 0 # 10//2 =5
# 5%2 = 1 # 5//2 =2
# 2%2 = 0 # 2//2=1
# 1%2=1 # 1//2=0
while n>0:
    list.append(n%2)
    n//=2
list.reverse()
print (list)
# 26 Дано число. Составить список чисел Фибоначчи, в том числе для отрицательных индексов. 
#  Т е для k = 5, список будет выглядеть так: [5, −3,  2, −1,  1, 0, 1, 1, 2, 3, 5]
# 27 Строка содержит набор чисел. Показать большее и меньшее число
with open('file.txt', 'r') as f:
    nums = f.read().split()
print(nums)
print(min(nums))
print(max(nums))


# 28 Найти корни квадратного уравнения Ax² + Bx + C = 0
# Математикой
import math

print("Введите коэффициенты для уравнения")
print("ax^2 + bx + c = 0:")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
 
discr = b ** 2 - 4 * a * c
print("Дискриминант D = %.2f" % discr)
 
if discr > 0:
    x1 = (-b + math.sqrt(discr)) / (2 * a)
    x2 = (-b - math.sqrt(discr)) / (2 * a)
    print("x1 = %.2f \nx2 = %.2f" % (x1, x2))
elif discr == 0:
    x = -b / (2 * a)
    print("x = %.2f" % x)
else:
    print("Корней нет")

# Используя дополнительные библиотеки*
# 29 Найти НОК двух чисел


a, b = 7, 51
i = min(a, b)
while True:
    if i%a==0 and i%b==0:
        break
    i += 1
print(i)




# 30 Вычислить число  c заданной точностью d
# 	Пример: при d = 0.001,  = 3.141. 10-1d10-10

# 31 Составить список простых множителей натурального числа N
v=[]
n=32

# def natur (n):
    # v=[i for i in range(1,n+1) if not n%i]
for i in range(1,n+1):
    for j in range(1, i):
        if not n%i and not i%j: v.append(i)
           
    # for i in range(len(v)):
    #     if v[i]%v[1]: v.pop(2)
    # return v
print (v)




# #13 Пользователь задаёт две строки. Определить количество количество вхождений одной строки в другой.

# def pere(one_str, two_str):
#     if (one_str in two_str):
#         count=0
#         setting=''
#         for i in range (len(two_str)-len(one_str)+1):
#             for j in range(len(one_str)):
#                 setiing=setting+two_str[i+1]
#                 if (setting == one_str):count+=1
#                 setting =''
#             return count
#             else:return False

# one_stre=input()
# two_stre=input()
# print(pere(one_stre, two_stre))

# def str_to_set(f)
#     res=set[]
#     for e in range (0, len(f)):
#         res.add(f(e))
#     return (res)
# c=()

# 14

# from random import randint
# x=2.8543
# def sum_off_num (a):
#     # b=str(a)
#     res=0
#     for i in str(a):
#         if i !='.': res+=int(i)
#     return res
#     print(res)
# print (sum_of_number(x))


# 15 Написать программу получающую набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда
# [ 1, 2, 6, 24 ]
# from turtle import xcor
# def prog1(N):
#     x=1
#     result=[]
#    for i in range(1,N+1):
#         x=i*x
#         result.append(x)
#     return result
# print(progr1(4))


