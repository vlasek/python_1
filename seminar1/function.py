def print_matrix (array):
    for i in range(len(array)): 
        for j in range(len(array[i])):
            print(array[i][j], end=' ')
        print()