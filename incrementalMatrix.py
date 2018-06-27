#!/usr/bin/env

"""
1
2 3
4 5 6
7 8 9 10
"""
n = 4
sum = 0
for i in range(n):
    for j in range(i + 1):
        sum+=1
        print (sum,end=' ')

    print()
