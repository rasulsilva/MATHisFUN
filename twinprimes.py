# -*- coding: utf-8 -*-

'''
Rasul Silva
DATE: 11/05/17
category: MATH FUN
Visualization of twin prime positioning

Description: A twin prime is any prime number that is distance 2 away from another
prime number. The Twin Prime Conjecture begs the following question: are there an 
infinite number of twin primes in existence? A program cannot prove or disprove
this conjecture because infinity is out of reach, but it may useful to visualize 
twin primes on a plot. What follows is just that! (: 
'''

import matplotlib.pyplot as plt
import math

#returns set of primes that exist from 0 to input(rangetop)
def findprimes (rangetop):
    primes = []
    for x in range(0,rangetop+1):
        divisorexists = 0
        #note: evens can also be skipped
        for w in range(2,int(math.ceil(x**.5))):#check all the way up to square root
            if x%w == 0: 
                divisorexists = 1 #divisor does exist, set boolean to 1 and break out       
                break
        if not divisorexists: #if divisor does not exist then the number is prime
            primes.append(x)
    return primes#all prime numbers in the range given

#find twin primes from a list of primes
def findtwins (primelist):
    twins = []
    i = 0
    while (i < len(primelist)-1):
        diff = primelist[i+1] - primelist[i]#calculate difference between adjacent items
        if diff == 2:#check for twin condition, if so add them to list then jump over them both (i+2)
            twins.append(primelist[i])
            twins.append(primelist[i+1])
            i = i + 2
        else:
            i = i + 1 # otherwise check next 
    return twins#all twin primes in list given

#generate list of numbers(rangelist) and a parallel list of numbers(score) containing 1 or 0 if the corresponding item in A is twin or not twin          
def genplotlists(twins, rangetop):
    
    rangelist = range(rangetop)#make ascending number list to check
    score = [None]*(rangetop)#create empty list
    for i, j in enumerate(rangelist):
        if j in twins:
            score[i] = 1# 1 if twin
        else:
            score[i] = 0# 0 if not twin
    
    return rangelist, score#rangelist = ascending number list
                           #score = 1 or 0 depending on if corresponding value in rangelist is twin or not twin
    
    
if __name__ == "__main__":
    
    rangetop = 1000
    primes = findprimes(rangetop) 
    twins = findtwins(primes)
    print("twin primes: ")
    print(twins)
    rangelist, score = genplotlists(twins, rangetop)
    
    plt.plot(rangelist, score)
    plt.ylabel('twin prime?')
    plt.xlabel('numbers 0 - %s' % str(rangetop))
    plt.title("twin prime grouping")
   
    '''
    note to self:
        sets of twin primes seem to be closer together at lower numbers and 
        farther apart at higher numbers. Other than that no predictable
        pattern is apparent
    '''
    


