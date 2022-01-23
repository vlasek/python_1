# 4 Найти максимальное из трех чисел

from random import randint 
list = [randint(1,100) for i in range(3)]
print(list)

max=list[0]
for i in range(1,3):
    if list[i]>max: max=list[i]

print (f'максимальное число - {max}')

# # def GetRandom(): 
# #     return l=randint(0,100)
# list=[]
# for i in range (3):
#     list=randint(0, 10)
#     print (list)

# print (list)

# # def PrintArray (array):
# #     while i<3: print (A[i])


# # for i in range (1,n+1):

# # F=F*

# # int i=0; //лучше делать через for  так не будет проблем с реопредлением i

# # i=0;


# # int max=0;
# # int[] A = new int [3];

# # while (i<3)

# # {

# # A[i]=GetRandom();

# # i++;

# # }

# # i=0;
# # max=A[i];

# # while (i<3)

# # {   if (A[i]>max) max=A[i];
# #   i++;

# # }


# # Console.Write ("В массиве: ");
# # i=0;
# # PrintArray(A);
# # Console.WriteLine();
# # Console.WriteLine("Максимальное число "+ max);
