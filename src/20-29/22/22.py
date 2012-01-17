'''
Created on Jan 13, 2011

@author: Jeff Patti
'''

names = []
with open("names.txt") as f:
    names_dirty = f.readline().split(',')
    for name in names_dirty:
        names.append(name[1:-1])

names.sort()


def compute_name_value(name, row):
    sum = 0
    for i in name:
            sum += ord(i)-ord("A")+1
    return sum*row


row = 1
sum = 0
for name in names:
    sum += compute_name_value(name, row)
    row += 1
    
print sum
    