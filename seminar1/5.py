# 5 Написать программу вычисления значения функции y = f(a)

def Function(a):
    y = a * a
    return y

print("Введите число перменную a: ")
a = int (input())
print ("Ваш ответ", Function(a))