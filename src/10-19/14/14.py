'''
Created on Jan 11, 2011

@author: Jeff Patti
'''

memo = {1:1}


def collatz(n):
    if n in memo:
        return memo[n]
    
    if n%2==0:
        value = collatz(n/2)+1
    else:
        value = collatz(3*n + 1) + 1
    memo[n]=value
    
    return value

longest_length = 0
longest_number = 0

for i in range(1,1000000):
    if i%10000==0:
        print i, (i/1000000.0)*100
    length = collatz(i)
    if length > longest_length:
        longest_length = length
        longest_number = i
        
print longest_length, longest_number
