# 27 Определить количество цифр в числе

def numbers_of_digit (b):
    num=0
    while (b>0):
        b=b//10
        num+=1
    return num

print (numbers_of_digit(223423))