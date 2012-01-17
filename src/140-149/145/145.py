'''
Created on Jan 13, 2012

@author: Jeff Patti
'''
import time

def is_reversible(n):
    if n%10==0:
        return False
    
    copy = n
    
    reverse = 0
    while copy>0:
        reverse *= 10
        reverse += copy%10
        copy /=10

    s = n+reverse
    
    while s>0:
        if s%2==0:
            return False
        s/=10
        
    return True

start_time = time.time()

count = 0
for i in xrange(10**9):
    if(is_reversible(i)):
        count+=1
        
print count
print time.time()-start_time


#not fast enough to be under the 1 minute rule, but it does the job...