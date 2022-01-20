# 10 Показать вторую цифру трёхзначного числа

import random
a=random.randint(100,1000)

print (a)
a=int(a/10)
print(int(a%10))