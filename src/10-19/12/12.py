'''
Created on Jan 12, 2011

@author: Jeff Patti
'''

import useful_functions
import time


number = 1

start = time.time()

while True:
    triangleNumber = sum(range(1, number+1))
  
    divisors = useful_functions.computeDivisors(triangleNumber)
    
    if len(divisors)>500:
        print triangleNumber, len(divisors)
        break
    
    number+=1

print "Took", (time.time()-start)
    
    
