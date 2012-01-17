'''
Created on Jan 15, 2011

@author: Jeff Patti
'''

import itertools
import math

def prime_sequence():
    primes = [2]
    yield 2
    
    next = 3
    while True:
        sqrt = int(math.sqrt(next));
        isPrime = True
        for i in primes:
            if i>sqrt:
                break
            if next%i==0:
                isPrime = False
                break
            
        if isPrime:
            yield next
            primes.append(next)            
            
        next+=2

primes = []

prime_gen = prime_sequence()
while True:
    next = prime_gen.next()
    primes.append(next)
    if next > 30000:
        break

def lazy_prime_sequence():
    global primes
    for i in primes:
        yield i

def primeFactor(n):
    
    primes = lazy_prime_sequence()
    
    result = []
    
    while n > 1:
        next_prime = primes.next()
        
        while n%next_prime == 0:
            result.append(next_prime)
            n/=next_prime
    return result

def computeDivisors(n):
    factors = primeFactor(n)
    factors.append(1)
    
    divisors = set() 
    
    mult = lambda x,y: x*y
    
    for i in range(1,len(factors)+1):
        for factor_subsample in itertools.combinations(factors,i):
            prod = reduce(mult,factor_subsample)
            divisors.add(prod)
    
    return divisors




def is_abundant(n):
    total = sum(computeDivisors(n))
    total -= n
    return total > n


abundant = []

for i in range(1,28123):
    if is_abundant(i):
        print i
        abundant.append(i)
print abundant

abundant_sums = set()
for abundant_subsample in itertools.combinations(abundant,2):
    abundant_sums.add(sum(abundant_subsample))
    
for i in abundant:
    abundant_sums.add(2*i)

print abundant_sums    

final_total = 0
for i in range(28124):
    if i not in abundant_sums:
        final_total+=i
        
print final_total
