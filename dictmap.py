#!/usr/bin/env python

N = int(input())
listdict = []
keys = ['Name', 'PhoneNumber']
for i in range(N):
    text = list(map(str, input().rstrip().split()))
    listdict.append(dict(zip(keys, text)))

for i in range(N):
    k = 0
    name = str(input())
    for j in listdict:
        if j["Name"] == name and 'PhoneNumber' in j:
            k = 1
            outstr = j["Name"] + "=" + j["PhoneNumber"]
            print(outstr)
    if k == 0:
        print("Not found")