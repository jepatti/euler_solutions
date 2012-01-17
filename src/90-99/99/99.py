'''
Created on Jan 12, 2011

@author: Jeff Patti
'''

import math

triples = []
row = 1
with open("base_exp.txt") as f:
    for line in f:
        parts = line.split(',')
        triple = [row, int(parts[0]), int(parts[1])]
        triples.append(triple)
        row+=1

max_value = 0
max_row = 0

for triple in triples:
    row = triple[0]
    a = triple[1]
    b = triple[2]
    
    value = b*math.log(a)
    
    if value>max_value:
        max_value = value
        max_row = row
print max_row