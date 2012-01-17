'''
Created on Jan 11, 2011

@author: Jeff Patti
'''

import useful_functions

primes = useful_functions.prime_sequence()


sum = 0
while True:
    next = primes.next()
    if next > 2000000:
        break
    sum+=next
print sum