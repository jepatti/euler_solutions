'''
Created on Jan 19, 2011

@author: Jeff Patti
'''

import useful_functions

does = set()

does.add(89)

does_not = set()

does_not.add(1)

def reach81(n, top):
    global does, does_not
    
    if n in does:
        return True
    if n in does_not:
        return False      
      
    digits = useful_functions.digits(n)
    square = lambda x : x*x
    new_n = sum(map(square, digits))
    
    if reach81(new_n, False):
        if not top:
            does.add(n)
        return True
    else:
        if not top:
            does_not.add(n)
        return False       


how_many = 0        
for i in range(1,10000000):
    if i%10000==0:
        print i, len(does), len(does_not)
    if reach81(i, True):
        how_many += 1
print "how many", how_many