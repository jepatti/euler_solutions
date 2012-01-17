'''
Created on Jan 11, 2011

@author: Jeff Patti
'''

import math
import itertools

def fibonacci_sequence():
    a,b = 1,1
    while True:
        yield b
        a,b=b,a+b

memoized_primes = {}
        
def prime_test(n):
    #if n in memoized_primes:
    #    return memoized_primes[n]
    
    if n == 1:
        return False
    sqrt = int(math.sqrt(n))
    for i in range(2,sqrt+1):
        if n%i==0:
            #memoized_primes[n]=False
            return False
        
    #memoized_primes[n]=True
    return True

        
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

def reverse(n):
    return int(str(n)[::-1])

def isPalindrom(s):
    return s == s[::-1]        
        
#def isPalindrom(s):
#    if len(s)<=1:
#        return True
#    if s[0]==s[-1]:
#        return isPalindrom(s[1:-1])
#    else:
#        return False


#def computeDivisors(n):
#    result = []
#    for i in range(1,n+1):
#        if n%i==0:
#            result.append(i)
#    return result


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

memo_factors={1:[]}
last_prime = 2
primeFactor2Primes = None

def primeFactor2(n):
    global last_prime, primeFactor2Primes
    primeFactor2Primes = prime_sequence()
    last_prime = 2
    
    return primeFactor2Helper(n)


def primeFactor2Helper(n):
    global last_prime, primeFactor2Primes
        
    if n in memo_factors:
        return memo_factors[n][:]
    
    result = []
    
    if n%last_prime == 0:
        using_factor = last_prime
        lower_factors = primeFactor2Helper(n/using_factor)
        lower_factors.append(using_factor)
        result = lower_factors
        
    else:
        while True:
            
            next_prime = primeFactor2Primes.next()
        
            if n%next_prime == 0:
                last_prime = next_prime
                lower_factors = primeFactor2Helper(n/next_prime)
                lower_factors.append(next_prime)
                result = lower_factors
                
                break
            
    memo_factors[n]=result        
    return result
    
        
def primeFactor(n):
    
    primes = prime_sequence()
    
    result = []
    
    while n > 1:
        next_prime = primes.next()
        
        while n%next_prime == 0:
            result.append(next_prime)
            n/=next_prime
    return result
            
def computeFactorial(n):
    if n==0 or n == 1:
        return 1
    
    return n*computeFactorial(n-1)

def choose(n,r):
    return computeFactorial(n)/(computeFactorial(r)*computeFactorial(n-r));

def digits(n):
    result = []
    while n > 0:
        result.append(n%10)
        n/=10
    result.reverse()
    return result
    