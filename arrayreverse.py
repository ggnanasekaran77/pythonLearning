#!/usr/bin/python

n = int(input().strip())
arr = []
for _ in range(n):
    arr_one = [int(arr_temp) for arr_temp in input().strip().split(' ')]
    arr.append(arr_one)
#n = 4
#arr = [1, 2, 3, 4]
str = str(" ".join(map(str, arr)))
str = str.replace(']', '')
str = str.replace('[', '')
str = str.replace(',', '')
print(str[::-1])
