'''
Created on Jan 12, 2012

@author: Jeff Patti
'''
cells = 20
array = [[0 for _ in range(cells+1)] for _ in range(cells+1)]

for i in range(cells+1):
    array[0][i]=1
    array[i][0]=1

for i in range(1,cells+1):
    for j in range(1,cells+1):
        array[i][j] = array[i-1][j] + array[i][j-1]

for line in array:
    print line
    
