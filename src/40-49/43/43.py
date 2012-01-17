'''
Created on Feb 4, 2011

@author: Jeff Patti
'''
import itertools

numbers = [0,1,2,3,4,5,6,7,8,9]
results = []
for d in itertools.permutations(numbers):
    if not d[3]%2==0:
        continue
    
    if not ((d[2]+d[3]+d[4])%3==0):
        continue
    
    if not d[5]%5==0:
        continue
    
    if not (d[4]*100+d[5]*10+d[6])%7==0:
        continue
    
    if not (d[5]*100+d[6]*10+d[7])%11==0:
        continue
    
    if not (d[6]*100+d[7]*10+d[8])%13==0:
        continue

    if not (d[7]*100+d[8]*10+d[9])%17==0:
        continue
    
    print d
    results.append(d)
    
total = 0
for result in results:
    total += int(''.join(map(str, result)))
print total