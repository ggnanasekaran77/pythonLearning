#!/bin/python3

import sys


#n = int(input().strip())
#arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
n = 4
arr = [1, 2, 3, 4]
str = str(" ".join(map(str, arr)))
print(str[::-1])
