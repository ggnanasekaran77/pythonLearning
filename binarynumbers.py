#!/usr/bin/env python
import sys

print("Hello World")

n = int(input().strip())
a = []
while n >= 1:
    a.append(n%2)
    n = n // 2
j = 0
b = []
for i in a:
    if i == 1:
        b.append(0)
        b[j] = b[j] + 1
    else:
        b.append(0)
        j += 1
print(max(b))
print()