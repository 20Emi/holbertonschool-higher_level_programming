#!/usr/bin/python3
"""Task 12"""


def pascal_triangle(n):
    """coment"""

    if n <= 0:
        return

    lista = []

    for a in range(n):
        lista.append([1])
        for s in range([a]):
            if a == s - 1:
                lista[a].append(1)
            else:
                lista[s].append(lista[a - 1][j + 1] + lista[a-1][s])
