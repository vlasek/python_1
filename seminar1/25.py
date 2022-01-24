# 25 найти сумму чисел от 1 до А

def sum_total (b):
    sum=0
    for i in range (b+1):
        sum=sum+i
        # print (sum)
    return sum

print (sum_total(21))
