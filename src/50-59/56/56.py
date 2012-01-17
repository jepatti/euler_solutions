'''
Created on Jan 14, 2011

@author: Jeff Patti
'''



def digits(n):
    result = []
    for i in str(n):
        result.append(int(i))
    return result

def digital_sum(n):
    return sum(digits(n))

max = 0

for a in range(1,101):
    for b in range(1,101):
        result = digital_sum(a**b)
        if result > max:
            max = result
            print a, b, max
        