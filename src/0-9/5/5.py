'''
Created on Jan 11, 2011

@author: Jeff Patti
'''

divisors = []
#2
divisors.append({2:1})

#3
divisors.append({3:1})

#4
divisors.append({2:2})

#5
divisors.append({5:1})

#6
divisors.append({2:1, 3:1})

#7
divisors.append({7:1})

#8
divisors.append({2:3})

#9
divisors.append({3:2})

#10
divisors.append({2:1,5:1})

#11
divisors.append({11:1})

#12
divisors.append({2:2, 3:1})

#13
divisors.append({13:1})

#14
divisors.append({2:1, 7:1})

#15
divisors.append({3:1, 5:1})

#16
divisors.append({2:4})

#17
divisors.append({17:1})

#18
divisors.append({2:1,3:2})

#19
divisors.append({19:1})

#20
divisors.append({2:2,5:1})


print divisors

max_powers = {2:1, 3:1, 5:1, 7:1, 11:1, 13:1, 17:1, 19:1}
for a_nums_divisors in divisors:
    for key, value in a_nums_divisors.iteritems():
        if max_powers[key] < value:
            max_powers[key] = value
print max_powers
result = 1
for key, value in max_powers.iteritems():
    result *= key**value
print result

    