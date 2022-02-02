# 5 Написать программу вычисления значения функции y = f(a)

def Function(a):
    y = a * a
    return y

a = float (input('Введите число перменную a: (для функции a в квадрате) '))
print ("Ваш ответ", Function(a))