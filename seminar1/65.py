# 65 Спирально заполнить двумерный массив:

# //   1  2  3  4
# //  12 13 14  5
# //  11 16 15  6
# //  10  9  8  7 

def print_matrix (array):
    for i in range(len(array)): 
        for j in range(len(array[i])):
            print(array[i][j], end=' ')
        print()

row = 3
col = 8
array = [[0  for i in range (col)] for j in range (row)]
print_matrix(array)


startRow = 1
startCol = 1
endRow = row
endCol = col
number = 2
while (number < row * col):
    for j in range (startCol-1, endCol-1):
        array[startRow-1][j] = number
        number += 1
    for i in range (startRow-1, endRow-1):
        array[i][endCol-1] = number
        number += 1
    for j in range (endCol-1, startCol-1, -1):
        array[endRow-1][j] = number
        number += 1
    for i in range (endRow-1, startRow-1, -1):
        array[i][startCol-1] = number
        number += 1
    startRow += 1
    startCol += 1
    endRow -=1
    endCol -=1

print_matrix(array)        







# int[,] Zadanie65New(int row, int col)
# {
#     int[,] array = Create2DArray(row, col);
#     int number = 1;

#     int startRow = 1, startCol = 1, endRow = row, endCol = col;

#     while (number < row * col)
#     {
#         // вправо
#         for (int j = startCol - 1; j < endCol - 1; j++)
#             array[startRow - 1, j] =
#             number++;

#         // вниз 
#         for (int i = startRow - 1; i < endRow - 1; i++)
#             array[i, endCol - 1] = number++;

#         // влево
#         for (int j = endCol - 1; j > startCol - 1; j--)
#             array[endRow - 1, j] = number++;

#         // вверх
#         for (int i = endRow - 1; i > startRow - 1; i--)
#             array[i, startCol - 1] = number++;

#         startRow++;
#         startCol++;
#         endRow--;
#         endCol--;
#     }

#     return array;
# }