# 22 Найти расстояние между точками в пространстве 2D/3D

# c2=a2+b2
import math
def Distanse(x1, y1, x2, y2):
    return math.sqrt(math.pow(x2-x1,2)+math.pow(y2-y1,2));
print (Distanse(0,0,5,5))