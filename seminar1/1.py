a=int(input('a= '))
b=int(input('b= '))
def check_sqrt(a,b):
    if a**2==b or b**2==a: print ('Числа является квадратом второго')
    else: print ('Число не квадрат другого')

check_sqrt(a, b)