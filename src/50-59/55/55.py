'''
Created on Feb 4, 2011

@author: Jeff Patti
'''

import useful_functions

def is_lychrel(n,depth):
    if depth>60:
        return False
    
    s = str(n)
    if depth != 0 and useful_functions.isPalindrom(s):
        return True

    #reverse s
    s_r = s[::-1]
        
    n_r = int(s_r)
    
    return is_lychrel(n+n_r,depth+1)
    
    
    
    
    
num = 0    
    
for i in range(10000):
    if not is_lychrel(i,0):
        num += 1
print num