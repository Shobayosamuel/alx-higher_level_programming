#!/usr/bin/python3
"""Divide the matrix"""


def matrix_divided(matrix, div):
    """DIvide the matrix

    Args:
        matrix (list): must be a list
        div (int): number to divide the matrix

    Raises:
        TypeError: should be raised if the correct type is not inserted
        TypeError: should be raised if the correct type is not inserted
        TypeError: should be raised if the correct type is not inserted
        ZeroDivisionError: is raised if div is 0

    Returns:
        list: new list after division
    """
    length = 0
    width = 0
    len_mat = len(matrix)
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                    for ele in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new = [list(map(lambda x: round(x / div, 2), row)) for row in matrix]
    return (new)
