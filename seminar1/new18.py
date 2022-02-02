# Реализовать алгоритм перемешивания списка. 

from random import randint
new_array = [i for i in range(10)]
print(new_array)

def mixing_list(x):
    for i in range (len(x)-1):
        # number = x[i]
        index = randint(i+1, len(x)-1)
        x[i], x[index] =  x[index], x[i]
        # x[index]=number
    return x

print(mixing_list(new_array))