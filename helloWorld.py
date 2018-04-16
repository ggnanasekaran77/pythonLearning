#!/usr/bin/env python



if __name__ == '__main__':
    t = int(input())
    evenstr = ""
    oddstr = ""
    instr = ""
    for arr in range(t):
        instr = input().rstrip()
        i = 0
        for j in instr:
            if i == 0:
                evenstr = evenstr + j
                i += 1
            elif i % 2 == 0:
                evenstr = evenstr + j
                i += 1
            else:
                oddstr = oddstr + j
                i += 1
        print(evenstr,oddstr)