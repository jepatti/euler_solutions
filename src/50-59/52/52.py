'''
Created on Jan 12, 2011

@author: Jeff Patti
'''


def does_this_do_it(n):
    a = n
    b = 2*n
    c = 3*n
    d = 4*n
    e = 5*n
    f = 6*n
    
    #print a, b, c, d, e, f
    
    a = convert_number_to_digit_array(a)
    b = convert_number_to_digit_array(b)
    c = convert_number_to_digit_array(c)
    d = convert_number_to_digit_array(d)
    e = convert_number_to_digit_array(e)
    f = convert_number_to_digit_array(f)
    
    a.sort()
    b.sort()
    c.sort()
    d.sort()
    e.sort()
    f.sort()
    
    #print a, b, c, d, e, f
    
    return a == b and b == c and c == d and d == e and e == f
    
    
def convert_number_to_digit_array(n):
    result = []
    for i in str(n):
        result.append(i)
    return result
    
i = 1
while True:
    if does_this_do_it(i):
        print i
        break
    i+=1
