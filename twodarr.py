#!/bin/python3

import sys

def flippingMatrix(matrix):
    # Complete this function
    for c in range(n):
        for r in range(n):
            temp = matrix[r][c*2]
            matrix[r][c * 2] = matrix[2 * n - 1 - r][c * 2]
            matrix[2 * n - 1 - r][c * 2] = temp
    sum = 0
    for r in range(n):
        for c in range(n):
            sum += matrix[r][c]

    return int(sum)

if __name__ == "__main__":
    #q = int(input().strip())
    #for a0 in range(q):
    #    n = int(input().strip())
    q = 1
    n = 2
    matrix = [[1, 2, 3, 4],[5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
       # matrix = []
        #for matrix_i in range(2*n):
        #  matrix_t = [int(matrix_temp) for matrix_temp in input().strip().split(' ')]
        #   matrix.append(matrix_t)
    result = flippingMatrix(matrix)
    print(result)