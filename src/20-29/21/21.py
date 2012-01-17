'''
Created on Jan 12, 2011

@author: Jeff Patti
'''

import useful_functions

def d(n):
    divisors = useful_functions.computeDivisors(n)
    return sum(divisors)-n

amicable_numbers = set()

for i in range(2,10000):
    
    if d(d(i)) == i:
        
        if i == d(i):
            continue
        
        print i, d(i)
        amicable_numbers.add(i)
        
        
print sum(amicable_numbers)
    