'''
Created on Jan 14, 2011

@author: Jeff Patti
'''

import useful_functions

distance = 0


index = 0
for i in range(1,1000000):
    digits = useful_functions.digits(i)
    while len(digits)>0:
        index += 1
        digit = digits[0]
        digits = digits[1:]
        if index == 1:
            print "1", digit
        if index == 10:
            print "10", digit
        if index == 100:
            print "100", digit
        if index == 1000:
            print "1000", digit
        if index == 10000:
            print "10000", digit
        if index == 100000:
            print "100000", digit
        if index == 1000000:
            print "1000000", digit
            break                                                