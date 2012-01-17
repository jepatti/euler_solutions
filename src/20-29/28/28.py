'''
Created on Jan 14, 2011

@author: Jeff Patti
'''

#for center
sum = 1
for i in range(1,501):
    #4x^2+4x+1
    sum += 4*i*i + 4*i + 1
    
    #4x^2 - 2x + 1
    sum += 4*i*i - 2*i + 1
    
    #4x^2 + 1
    sum += 4*i*i + 1
    
    #4x^2 + 2x + 1
    sum += 4*i*i + 2*i + 1
    
print sum  