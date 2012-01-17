'''
Created on Jan 15, 2011

@author: Jeff Patti
'''

from fractions import Fraction

d_max = 1000000

target = Fraction(3,7)
closest = Fraction(1,3)
for d in range(4,d_max+1):
    x = (3*d)/7
    result = Fraction(x,d)
    if result < target and result > closest:
        closest = result
print closest 
        
    
