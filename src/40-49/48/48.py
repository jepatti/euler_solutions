'''
Created on Jan 12, 2011

@author: Jeff Patti
'''

self_raise = lambda x:x**x
print str(sum(map(self_raise, range(1,1001))))[-10:]





