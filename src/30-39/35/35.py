'''
Created on Jan 14, 2011

@author: Jeff Patti
'''

import useful_functions

prime_gen = useful_functions.prime_sequence()



primes = set()

while True:
    next = prime_gen.next()
    if next > 1000000:
        break
    primes.add(next)


circular = set()

for i in primes:
    nums = str(i)
    for shift in range(len(nums)):
        nums = nums[1:]+nums[0]
        if int(nums) not in primes:
            break
    else:
        circular.add(i)
print len(circular)