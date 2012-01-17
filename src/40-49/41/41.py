'''
Created on Jan 13, 2012

@author: Jeff Patti
'''
import itertools
import useful_functions

#can't have a 9 or 8 digit pandigital prime number, the numers 1--8 (and 1--9) sum up to a multiple of 3
#meaning, all numbers composed of those digits can not be prime.
#fails 3 prime test

orig = '7654321'

for perm in itertools.permutations(orig):
    num = int(''.join(perm))
    if useful_functions.prime_test(num):
        print num