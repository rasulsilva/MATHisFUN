'''
Rasul Silva
10/17/17
category: MATH FUN
Goldbach conjecture visualization


Description: The Goldbach conjecture states that any even number
greater than 2 is the sum of 2 primes. For every even integer,
this program calculates the pairs of primes that sum to the even 
target. I wrote this program to see if there was any recognizable 
pattern that could be useful. The produced graph displays the even
target on the x axis and the addend values on the y axis.
'''

import matplotlib.pyplot as plt
import math
import numpy as np

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

def generate_evens (rangetop):
    i=4
    evens = []
    while (i<=rangetop):
        evens.append(i)
        i+=2
    return evens    

def MergeSort(numlist):
    sortedlist = np.sort(numlist, kind = 'mergesort')
    return sortedlist.tolist()

def BinarySearch(sortedlist, target):
    first = 0
    last = len(sortedlist) - 1
    while first <= last:
        midpoint = (first + last)//2
        #print("midpoint: %d" % midpoint)
        if target == sortedlist[midpoint]:
            return midpoint
        elif target > sortedlist[midpoint]:
            first = midpoint + 1
        else:
            last = midpoint - 1
    return 0    

#returns the last index that is <= target
def checkforbiggerthan(numlist, target): 
    for i,j in enumerate(numlist):
        if j > target:
            return i-1
    return 0    

#this function produces all prime addend combinations that sum to every even number
def addendfinder(rangetop):
    primes = generate_prime_list(rangetop)
    evens = generate_evens(rangetop)
    #print(primes)
    #print(evens)
    firstaddend = []
    secondaddend = []
    eventarget = []
    for num in evens:
        #print("num: " + str(num))
        tempprimes = primes
        #print("primes: " + str(tempprimes))
        specindex =  checkforbiggerthan(tempprimes, num)
        #print("specindex: " + str(specindex))
        tempprimes = tempprimes[0:specindex]
        #print("updated tempprimes: " + str(tempprimes))
        for i,j in enumerate(tempprimes):
            w = BinarySearch(tempprimes,num - j)
            #print("w: " + str(w))
            if w != 0:
                firstnum = j
                secondnum = tempprimes[w]
                #print ("firstnum,secondnum : " + str(j) + "," + str(w))
                #print("eventarget: " + str(num))
                firstaddend.append(firstnum)
                secondaddend.append(secondnum)
                eventarget.append(num)
                
    return firstaddend,secondaddend, eventarget
                
            
if __name__ == "__main__":
    
     firstaddend, secondaddend, eventarget = addendfinder(1000)
     print("first addend:   " + str(firstaddend))
     print("second addend:  " + str(secondaddend))
     print("even target:  " + str(eventarget))
    
     plt.plot(eventarget, firstaddend, 'bs', eventarget, secondaddend,'g^')
     plt.ylabel('addends')
     plt.xlabel('even targets')
     plt.title("Goldbach")
    
    

    
    
    
    
        
