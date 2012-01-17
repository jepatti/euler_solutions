'''
Created on Jan 12, 2011

@author: Jeff Patti
'''

import calendar


sundays = 0
c = calendar.Calendar(6)


for year in range(1901,2001):
    for month in range(1,13):
        ci = c.itermonthdays(year, month)
        if ci.next()==1:
            sundays+=1
print sundays