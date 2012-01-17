'''
Created on Feb 4, 2011

@author: Jeff Patti
'''



#compute the 2 part

value = 1

for i in range(7830457):
    value*=2
    value %=10**10
print value

print value*28433 + 1