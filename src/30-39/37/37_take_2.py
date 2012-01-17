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

legal_lefts = [23, 29, 31, 37, 53, 59, 71, 73, 79]


found = 0

total = 0

while True:
    
    print "legal lefts:", legal_lefts
    
    if len(legal_lefts) == 0:
        break
    
    for test in legal_lefts:
        if test_value(test):
            found += 1
            print test
            total += test

    
    new_legal_lefts = []
    
    for possible in legal_lefts:
        left_shifted = possible*10
        if useful_functions.prime_test(left_shifted+1):
            new_legal_lefts.append(left_shifted+1)
            
        if useful_functions.prime_test(left_shifted+3):
            new_legal_lefts.append(left_shifted+3)
            
        if useful_functions.prime_test(left_shifted+7):
            new_legal_lefts.append(left_shifted+7)
            
        if useful_functions.prime_test(left_shifted+9):
            new_legal_lefts.append(left_shifted+9)
        
    legal_lefts = new_legal_lefts
        

print "total", total
    