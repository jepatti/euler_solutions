'''
Created on Feb 3, 2011

@author: Jeff Patti
'''

import useful_functions

def convert_number_to_new_base(n):
    numbers = ["1","3","7","9"]
    result = ""
    while True:
        r = n%4
        result = numbers[r] + result
        n/=4
        if n == 0:
            break
        n-=1
    return int(result)

def trunc_left_prime(n):
    if len(str(n)[1:])==1:
        return useful_functions.prime_test(int(str(n)[1:]))
    
    trunced = int(str(n)[1:])
    
    if not useful_functions.prime_test(trunced):
        return False
    
    return trunc_left_prime(trunced)

def trunc_right_prime(n):
    if len(str(n)[:-1])==1:
        return useful_functions.prime_test(int(str(n)[:-1]))
    
    trunced = int(str(n)[:-1])
    
    if not useful_functions.prime_test(trunced):
        return False
    
    return trunc_right_prime(trunced)

print "max value: ", convert_number_to_new_base(100000)

def test_value(n):
    digits = str(n)
    for i in range(1,len(digits)):
        v = int(digits[0:i])
        if not useful_functions.prime_test(v):
            return False

        v = int(digits[i:])
        if not useful_functions.prime_test(v):
            return False
    return True

for i in range(4,1000000):
    n = convert_number_to_new_base(i);
    if str(n)[0]=='1':
        continue
    
    if str(n)[-1]=='1':
        continue
    
    if useful_functions.prime_test(n) and test_value(n):
        print n
    
    
    