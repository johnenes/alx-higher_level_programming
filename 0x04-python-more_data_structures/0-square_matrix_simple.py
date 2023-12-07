#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    '#creating a new matrix with the same size as the input matrix'
    result = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

    '#Iterate through the matrix and computer the square of each element'
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            result[i][j] = matrix[i][j] ** 2

    return result
