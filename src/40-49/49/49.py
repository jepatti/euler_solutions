'''
Created on Feb 6, 2011

@author: Jeff Patti
'''

import useful_functions
from collections import defaultdict



prime_gen = useful_functions.prime_sequence()

prime_set = set()
prime_list = []
while True:
    val = prime_gen.next()
    if val > 30000:
        break
    prime_set.add(val)
    prime_list.append(val)
    

prime_groups = defaultdict(list)


    
for prime in prime_list:
    if prime < 1000:
        continue
    if prime > 10000:
        break
    prime_groups[''.join(sorted(str(prime)))].append(prime)
    

for group in prime_groups:
    group = prime_groups[group]
    if len(group)<3:
        continue
    group = sorted(group)

    
    for i in range(len(group)-2):
        first = group[i]
        second_offset = 1
        while True:
            if i+second_offset >= len(group):
                break            
            second = group[i+second_offset]
            third = 2*second - first
            if third in group:
                print group
                print first, second, third, str(first)+str(second)+str(third)
                
            second_offset+=1

