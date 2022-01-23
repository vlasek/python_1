# 20 Задать номер четверти, показать диапазоны для возможных координат

f=3
print(f'{f} четверть')
if f==1: print ('x>=0  y>0')
elif f==2: print ('x<0 and y>=0')
elif f==3: print('x<0 and y<=0')
elif f==4: print('x>=0 and y<0')
else: print ('неправильно введен номер четверти')