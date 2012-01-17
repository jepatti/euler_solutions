'''
Created on Jan 12, 2011

@author: Jeff Patti
'''
import useful_functions

high = 0

for i in range(1,101):
    for j in range(1,i):
        if useful_functions.choose(i,j)>1000000:
            high += 1

print high
        