'''
Created on Jan 15, 2011

@author: Jeff Patti
'''

import useful_functions

primes = set()

prime_generator = useful_functions.prime_sequence()

for i in range(2000):
    primes.add(prime_generator.next())
     
def how_many_primes(a, b):
    n = 0
    evaluate = lambda n, a, b : n*n + a*n + b  
    while True:
        iteration = evaluate(n,a,b)
        if iteration not in primes:
            return n
        n += 1
            
print how_many_primes(1, 41)

max_a = 0
max_b = 0
max_primes = 0
for a in range(-1000,1001):
    for b in range(-1000,1001):
        count = how_many_primes(a,b)
        if count > max_primes:
            max_primes = count
            max_a = a
            max_b = b
            print max_primes, max_a, max_b, max_a*max_b
        