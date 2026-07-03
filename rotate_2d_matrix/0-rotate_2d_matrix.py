#!/usr/bin/python3
"""
Module containing a function to rotate a 2D matrix 90 degrees clockwise.
"""


def rotate_2d_matrix(matrix):
    """
    Rotates an n x n 2D matrix 90 degrees clockwise in-place.

    Args:
        matrix (list of list of int): The square matrix to be rotated.
    """
    n = len(matrix)

    # 1. Transpose the matrix (swap matrix[i][j] with matrix[j][i])
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # 2. Reverse each row
    for i in range(n):
        matrix[i].reverse()
