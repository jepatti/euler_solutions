'''
Created on Jan 15, 2011

@author: Jeff Patti
'''

import sys

def tri_gen():
    n = 1
    while True:
        result = (n*n + n)/2
        n+= 1
        yield result

tris = []

tri = tri_gen()
while True:
    next = tri.next()
    if(next > 1000):
        break
    tris.append(next)

print tris

def letter_sum(word):
    return sum([ord(x)-ord("A") + 1 for x in word])
    
with open(sys.argv[1]) as f:
    words = []
    for line in f:
        for word in line.split(","):
            words.append(word[1:-1])
    number_of_tri_words = 0
    for word in words:
        word_sum = letter_sum(word)
        if word_sum in tris:
            number_of_tri_words+=1
            print word, word_sum
    print number_of_tri_words
        
        