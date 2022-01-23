# 24 Найти кубы чисел от 1 до N

n=int(input('введите N = '))
def cube (b):
    return b**3

for i in range (1, n+1):
    print(f'{i} - {cube(i)}')
    