#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    m = matrix
    return [list(map(lambda n: n*n, i)) for i in matrix]
