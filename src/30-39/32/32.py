'''
Created on Jan 16, 2012

@author: Jeff Patti
'''
import itertools

s = '123456789'

results = set()

for perm in itertools.permutations(s):
    for mult_index in range(4):
        index1 = 1+mult_index
        part1 = ''.join(perm[:index1])
        for equal_index in range(4):
            index2 = index1 + 1 + equal_index
            part2 = ''.join(perm[index1:index2])
            part3 = ''.join(perm[index2:])
            
            if len(part1) > len(part3) or len(part2) > len(part3):
                continue
            
            if int(part1) * int(part2) == int(part3):
                print part1, part2, part3
                results.add(int(part3))
            #print part1, "*", part2, '=', part3
print results
print sum(results)