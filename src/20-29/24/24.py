'''
Created on Jan 14, 2011

@author: Jeff Patti
'''

import itertools

index = 1
for i in itertools.permutations(range(10)):
    if index == 1000000:
        print i
        break
    index+=1
        