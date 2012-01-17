'''
Created on Jan 12, 2011

@author: Jeff Patti
'''

import useful_functions

fibo = useful_functions.fibonacci_sequence()

i = 0
while True:
    i+=1
    fibo_number = fibo.next()
    print i, fibo_number
    if len(str(fibo_number))==1000:
        print i
        break
print i+1