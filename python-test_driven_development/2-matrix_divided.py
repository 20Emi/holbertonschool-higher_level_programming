#!/usr/bin/python3

"""task 1: function that divides all elements of a matrix."""


def matrix_divided(matrix, div):
    """divide a matrix"""

    new_matr = []

    contx = "matrix must be a matrix (list of lists) of integers/floats"

    if type(matrix) is not list or len(matrix) == 0 or len(matrix[0]) == 0:
        raise TypeError(contx)
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    den = len(matrix[0])
    for fila in matrix:
        new = []
        if type(fila) is not list:
            raise TypeError(contx)
        if len(fila) != den:
            raise TypeError("Each row of the matrix must have the same size")
        for colonna in fila:
            if not isinstance(colonna, (int, float)):
                raise TypeError(contx)
            new.append(round(colonna/div, 2))
        new_matr.append(new)
    return new_matr

