'''
Created on Jan 11, 2011

@author: Jeff Patti
'''

def computeFactorial(n):
    if n == 1:
        return 1
    
    return n*computeFactorial(n-1)

sum = 0
for n in str(computeFactorial(100)):
    sum += int(n)
print sum