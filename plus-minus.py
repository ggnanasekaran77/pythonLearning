#!/usr/bin/env python

print("Hello World")

def plusminus(arr):
    print(round(len([x for x in arr if x > 0]) / n, 6))
    print(round(len([x for x in arr if x == 0]) / n, 6))
    print(round(len([x for x in arr if x < 0]) / n, 6))

if __name__ == '__main__':
    #n = int(input())
    #arr = list(map(int, input().rstrip().split()))
    n = 6
    arr = [ -4, 3, -9, 0, 4, 1 ]
    plusminus(arr)