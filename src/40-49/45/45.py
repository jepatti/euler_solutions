'''
Created on Jan 14, 2011

@author: Jeff Patti
'''


def tri_gen():
    n = 2
    while True:
        result = (n*n + n)/2
        n+= 1
        yield result

def pen_gen():
    n = 2
    while True:
        result = (3*n*n - n)/2
        n+= 1
        yield result
        
        
def hex_gen():
    n = 2
    while True:
        result = 2*n*n-n
        n+= 1
        yield result

tri = tri_gen()
pen = pen_gen()
hex = hex_gen()

t = tri.next()
p = pen.next()
h = hex.next()        
    
    
while True:
    #print t, p, h
    if t == p and p == h:
        print t
    
    if t <= p and t <= h:
        t = tri.next()
        continue;    
    
    if p <= t and p <= h:
        p = pen.next()
        continue;
    
    if h <= t and h <= p:
        h = hex.next()
        continue;