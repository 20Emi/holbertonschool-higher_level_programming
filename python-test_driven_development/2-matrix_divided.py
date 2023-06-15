#!/usr/bin/python3
"""task 1: function that divides all elements of a matrix."""


def matrix_divided(matrix, div):
    """divide a matrix"""

    new_matrix = matrix.copy()
    contx = "matrix must be a matrix (list of lists) of integers/floats"
    for fila in range(len(new_matrix)):
        aux = len(new_matrix[0])
        if aux != len(new_matrix[fila]):
            raise TypeError("Each row of the matrix must have the same size")
        for colonna in range(len(new_matrix[fila])):
            if div == 0:
                raise ZeroDivisionError("division by zero")
            if not isinstance(div, (int, float)):
                raise TypeError("div must be a number")
            if not isinstance(new_matrix, list):
                raise TypeError(contx)
            if not isinstance(new_matrix[fila][colonna], (int, float)):
                raise TypeError(contx)
            new_matrix[fila] = list(map(lambda x: round((x / div), 2),
                                        matrix[fila]))
    return new_matrix
