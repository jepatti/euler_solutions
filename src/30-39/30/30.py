'''
Created on Jan 14, 2011

@author: Jeff Patti
'''

def works(n, power):
    ds = digits(n)
    sum = 0
    for i in ds:
        sum += i**power
    return sum==n
        
    
    
def digits(n):
    result = []
    for i in str(n):
        result.append(int(i))
    return result





sum = 0
for i in range(2,1000000):
    if works(i,5):
        print i
        sum += i
        
print "Total:", sum