#!/usr/bin/env python

import sys

def factorial(n):
    # Complete this function
    if n <= 1:
        n = 1
        return int(n)
    else:
        return int(n*factorial(n-1))
if __name__ == "__main__":
    n = int(input().strip())
    res = 1
    result = factorial(n)
    print(result)
