# 41. Выяснить являются ли три числа сторонами треугольника


a = int(input('Введите первое число '))
b = int(input('Введите второе число '))
c = int(input('Введите третье число '))

def CheckTriangle(a, b, c):
    if (a+b > c and a+c > b and c+b > a): s='Это стороны треугольника'
    else:
        s='Это не стороны треугольника'
    return s
    

print(CheckTriangle(a, b, c))
