'''
Created on Jan 17, 2012

@author: Jeff Patti
'''
import useful_functions
import math

cons_sequence = 4

array_size = 1000000 #kept adding zeroes until it found the solution
array = [[] for _ in xrange(array_size)]

prime_generator = useful_functions.prime_sequence()
for prime in prime_generator:
    if prime > math.sqrt(array_size):
        break
    for multiple in xrange(prime, array_size, prime):
        array[multiple].append(prime)

for index in xrange(array_size):
    for slice_item in array[index:index+cons_sequence]:
        if len(slice_item)!= cons_sequence:
            break
    else:
        print index
        break
    

