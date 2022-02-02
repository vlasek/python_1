# 19 Реализовать алгоритм задания случайных чисел.
# Без использования встроенного генератора псевдослучайных чисел


import datetime


# def get_rand():
#     return datetime.datetime.now().microsecond % 100


#print ('19 задача ')

# def crt_arr_base_on_three(n):
#     return [(-3)**i for i in range(n+1)]

# print(crt_arr_base_on_three(5))


pip install qrcode
import qrcode
data = "https://alta-tour.ru"
filename = "site.png"
img = qrcode.make(data)
img.save(filename)
