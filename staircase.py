#!/usr/bin/env python

def staircase(n):
    for i in range(1,n+1):
        str=""
        for j in range(1,n+1):
            if j > n - i :
                str = str + "#"
        print(str.rjust(n))




if __name__ == '__main__':
    print("Hello World")
    #n = int(input())
    n = 6
    staircase(n)