
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

#check if num is prime: return True or False
def is_prime(num):
    if num == 0 or num == 1: return False
    if num % 2 == 0: return False
    for value in range(2,int(num**.5) + 1):
        if num % value == 0:
            return False
    return True

#generate list of prime numbers up to range_top
def generate_prime_list(range_top):
    primes = [2]
    for i in range(2,range_top+1):
        if (is_prime(i)):
            primes.append(i)
    return primes 

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
    
    rangetop = 6000
    primes = generate_prime_list(rangetop) 
    twins = findtwins(primes)
    print(primes)
    print("twin primes: ")
    #print(twins)
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
    


