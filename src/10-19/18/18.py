'''
Created on Jan 14, 2011

@author: Jeff Patti
'''

import sys

def prettyprint(n):
    for i in range(len(n)):
        print n[i]

data = []

f = open("triangle.txt")

for line in f.readlines():
    row = line.split()
    numbers = []
    for word in row:
        numbers.append(int(word))
    data.append(numbers);
    
print data

data.reverse()

prettyprint(data)
print

for i in range(len(data)-1):
    for j in range(len(data[i+1])):
        left = data[i][j]
        right = data[i][j+1]
        if left < right :
            left, right = right, left
        
        data[i+1][j]+=left
        
prettyprint(data)
print


