#!/usr/bin/env python

print("Hello World")

def digonalsumdiff (a):
    for i in range(n):
        for j in range(n):
            print(a[i][j],end=' ')
        print()

if __name__ == '__main__':
    #n = int(input())
    n = 3
    a = []
    #for _ in range(n):
    #    a.append(list(map(int, input().rstrip().split())))
    a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    result = digonalsumdiff(a)
    print(result)