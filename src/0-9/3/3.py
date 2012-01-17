'''
Created on Jan 11, 2011

@author: Jeff Patti
'''

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
        
        
primes = prime_sequence()



number = 600851475143

while True:
    prime = primes.next()
    
    while number % prime == 0:
        print prime
        number/=prime
    
    if prime>math.sqrt(number):
        print number
        break
    
 