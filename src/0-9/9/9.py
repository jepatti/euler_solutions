'''
Created on Jan 11, 2011

@author: Jeff Patti
'''

import math

running = True

for a in range(1000,0,-1):
    for b in range(1,1000):
        c = math.sqrt(a*a+b*b)
        
        c = int(c)
        
        #time to decrement a
        if a+b+c > 1000:
            break
        
        #we didn't find a triple
        if a*a+b*b-c*c != 0:
            continue
        
        if a+b+c==1000:
            print a, b, c, a*b*c
            running = False
            
    if not running:
        break

