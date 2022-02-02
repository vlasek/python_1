# 29 Написать программу вычисления произведения чисел от 1 до N

import random
num = random.randint(1, 10)
result = 1

for i in range(1, num + 1):
    result *= i

print(num, result)



n=5
F=1
for i in range (1,n+1):
    F=F*i
print (F)