'''
Created on Jan 13, 2012

@author: Jeff Patti
'''
from fractions import Fraction

result = Fraction(1,1)


for n in range(10,100):
    for d in range(n+1,100):
        orig_frac = Fraction(n,d)
        
        ns = str(n)
        ds = str(d)
        if ds[1] == '0':
            continue
       
        if not ( ns[0] in ds or ns[1] in ds ):
            continue
        
        if ns[0] in ds:
            if ns[0] == ds[0]:
                if ds[1] == '0':
                    continue
                new_frac = Fraction(int(ns[1]), int(ds[1]))  
            else:
                new_frac = Fraction(int(ns[1]), int(ds[0]))
        else:
            if ns[1]==ds[0]:
                if ds[1] == '0':
                    continue
                new_frac = Fraction(int(ns[0]), int(ds[1]))  
            else:
                new_frac = Fraction(int(ns[0]), int(ds[0]))               
        if orig_frac == new_frac:
            result *= new_frac
            print n,d
print result