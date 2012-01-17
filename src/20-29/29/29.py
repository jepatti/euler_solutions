'''
Created on Jan 13, 2011

@author: Jeff Patti
'''

prods = set()

for a in range(2,101):
    for b in range(2,101):
        prods.add(a**b)
print len(prods)