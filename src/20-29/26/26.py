'''
Created on Feb 6, 2011

@author: Jeff Patti
'''





def compute_cycle_length(n):
    prev = {}
    
    r = 1
    #print "0.",
    index = 0
    while r!=0:
        r*=10
        d=r/n
        r=r%n
        combined = str(d) + " " + str(r)
        if combined in prev:
            return index - prev[combined]
        prev[combined]=index        
        index += 1
        #print d,
    return 0

max_len = 0      
for i in range(2,1000):
    val = compute_cycle_length(i)
    if val > max_len:
        max_len = val
        print i