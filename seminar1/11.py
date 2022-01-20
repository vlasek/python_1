# 11 Дано число из отрезка [10, 99]. Показать наибольшую цифру числа

import random
a = random.randint(10, 99)
b = int(a/10)
c = a % 10
def maxdigit (a):
    if (b > c):return b
    else:return c

print("Случайное число ", a)
print ("макc цифра", maxdigit(a))

