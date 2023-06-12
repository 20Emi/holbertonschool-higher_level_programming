#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = matrix.copy()

    for matr in range(len(matrix)):
        new[matr] = list(map(lambda a: a**2, matrix[matr]))

    return new
