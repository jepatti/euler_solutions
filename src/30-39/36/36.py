'''
Created on Jan 14, 2011

@author: Jeff Patti
'''

import useful_functions


sum = 0
for i in range(1000000):
    decimal = str(i)
    binary = str(bin(i))[2:]
    
    if useful_functions.isPalindrom(decimal) and useful_functions.isPalindrom(binary):
        print decimal, binary
        sum += i
        
print sum