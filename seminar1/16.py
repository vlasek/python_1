# 16 Дано число обозначающее день недели. Выяснить является номер дня недели выходным

week = ['понедельник', 'вторник', 'среда',
        'четверг', 'пятница', 'суббота', 'воскресенье']
a = int(input())
if a==6 or a==7:
    print(week[a-1])
    print ("Day off")
else:
    print(week[a-1])
    print ("regular day")