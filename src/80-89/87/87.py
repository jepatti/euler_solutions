'''
Created on Jan 19, 2011

@author: Jeff Patti
'''

import useful_functions


prime_seq = useful_functions.prime_sequence()

primes = []

while True:
    next = prime_seq.next()
    if next>8000:
        break
    primes.append(next)

numbers = set()

for a in primes:
    for b in primes:
        for c in primes:
            number = c**2+b**3+a**4
            if number>=50000000:
                break
            numbers.add(number)
print len(numbers)