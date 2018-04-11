#!/usr/bin/env python

def solution (A):
    result = []
    for i in range(len(A) - 1):
        start = 0
        if A[i] == A[i+1]:
            pass
        elif A[i] < A[i+1]:
            if start == 0:
                result.append(int(i))
        else:
            start = 0

    res = ((''.join(map(str, result))))
    return int(res)






A = [2, 2, 2, 2, 1, 2, -1, 2, 1, 3]
print(solution(A))