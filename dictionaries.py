#!/usr/bin/env python

print("Hello World")
myDict = {}
myDict = {'key1': 'value1', 'key3' : 'value3'}
print(myDict)
for key in myDict:
    print(key, myDict[key])

keys = ['FirstName', 'LastName', 'SSID']

name1 = ['Michael', 'Kirk', '224567']
name2 = ['Linda', 'Matthew', '123456']

dictList = []
dictList.append(dict(zip(keys, name1)))
dictList.append(dict(zip(keys, name2)))

print (dictList)
for item in dictList:
    print (' '.join([item[key] for key in keys]))
    