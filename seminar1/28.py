# 28 Подсчитать сумму цифр в числе


def sum_of_digit (b):
    sum=0
    while (b>0):
        sum+=b%10
        b=b//10
    return sum

print (sum_of_digit(223))