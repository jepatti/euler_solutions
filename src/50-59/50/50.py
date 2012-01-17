'''
Created on Jan 16, 2012

@author: Jeff Patti
'''
import useful_functions

primes = []
prime_set = set()

prime_generator = useful_functions.prime_sequence()
for prime in prime_generator:
    if prime > 1000000:
        break
    primes.append(prime)
    prime_set.add(prime)

print primes
print len(primes)

num_primes = len(primes)

for j in range(20,1000):
    for i in range(len(primes)):
        if num_primes < i+j:
            continue
        
        slice = primes[i:i+j]
        #print slice
        summed = sum(slice)
        if summed > 1000000:
            break
        if summed in prime_set:
            print slice
            print summed, j
            break
        