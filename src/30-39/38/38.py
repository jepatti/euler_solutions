'''
Created on Jan 16, 2012

@author: Jeff Patti
'''
import itertools

results = []



for i in range(10000):
    temp_results = []
    total_len = 0
    all_digits = set()
    for multiplier in range(1,10):
        prod = i*multiplier
        
        temp_results.append(prod)
        
        s = str(prod)
        total_len += len(s)
        
        for d in s:
            all_digits.add(d)
            
        if total_len == 9:
            if len(all_digits)==9:
                if '0' in all_digits:
                    break
                results.append(''.join(map(str,temp_results)))
            else:
                break
        if total_len>9:
            break
print results
print max(results)
            