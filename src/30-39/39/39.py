'''
Created on Jan 21, 2011

@author: Jeff Patti
'''
import math
from collections import defaultdict

class triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        
    def __str__(self):
        return "%i %i %i" % (self.a, self.b, self.c)

def compute_right_triangles_with_c_of(c):
    triangles = []
    for a in range(1,c):
        remainder = c*c - a*a
        b = math.sqrt(remainder)
        b = int(b)
        if c*c - (a*a + b*b) == 0:
            t = sorted([a,b,c])
            triangles.append(triangle(t[0],t[1],t[2]))
    return triangles


all_triangles = set()

for i in range(2,1001):
    for t in compute_right_triangles_with_c_of(i):
        all_triangles.add(t)
    triangles = compute_right_triangles_with_c_of(i)


d = defaultdict(int)
for t in all_triangles:    
    p = t.a + t.b + t.c
    d[p] = d[p]+1
    
print d

max_p=0
max_p_value=0
for i in range(2,1001):
    if d[i]>max_p_value:
        max_p_value = d[i]
        max_p = i
print max_p
