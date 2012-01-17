'''
Created on Jan 14, 2011

@author: Jeff Patti
'''

import useful_functions


total = 0
for i in range(3,3000000):
    digits = useful_functions.digits(i)
    result = sum(map(useful_functions.computeFactorial, digits))
    if result == i:
        print i
        total += i
        
print "total:", total