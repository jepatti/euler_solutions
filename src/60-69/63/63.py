'''
Created on Jan 15, 2011

@author: Jeff Patti
'''

total = 0
for pow in range(1,30):
    for i in range(1,30):
        result = i**pow
        digits = len(str(result))
        if digits == pow:
            total += 1
            print i, pow, result
print total