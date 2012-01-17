'''
Created on Jan 11, 2011

@author: Jeff Patti
'''

def fibonacci_sequence():
    a,b = 1,1
    while True:
        yield b
        a,b=b,a+b

sum = 0
fibo = fibonacci_sequence()

while True:
    next = fibo.next()
    
    if next > 4000000:
        break
        
    if(next%2==0):
        sum+=next

print sum