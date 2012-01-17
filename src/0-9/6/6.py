'''
Created on Jan 11, 2011

@author: Jeff Patti
'''

square = lambda s:s*s

sum_of_squares = sum(map(square,range(100+1))) 

square_of_sum = square(sum(range(100+1)))

print square_of_sum - sum_of_squares