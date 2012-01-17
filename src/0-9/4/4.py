'''
Created on Jan 11, 2011

@author: Jeff Patti
'''

def isPalindrom(s):
    if len(s)<=1:
        return True
    if s[0]==s[-1]:
        return isPalindrom(s[1:-1])
    else:
        return False
    

max = 0

for i in range(1000):
    for j in range(1000):
        prod = i*j
        if isPalindrom(str(prod)) and prod > max:
            max = prod
            
print max