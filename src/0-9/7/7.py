'''
Created on Jan 11, 2011

@author: Jeff Patti
'''

import useful_functions


primes = useful_functions.prime_sequence()

for i in range(10000):
    primes.next()
    
print primes.next()