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

def findprimes (rangetop):
    primes = []
    for x in range(1,rangetop+1):
        divisorexists = 0
        #note: evens can also be skipped
        for w in range(2,int(math.ceil(x**.5) + 1)):#check all the way up to square root
            if x%w == 0: 
                divisorexists = 1 #divisor does exist, set boolean to 1 and break out       
                break
        if not divisorexists: #if divisor does not exist then the number is prime
            primes.append(x)
    return primes#all prime numbers in the range given

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

def checkforbiggerthan(numlist, target): #returns the last index that is <= target
    for i,j in enumerate(numlist):
        if j > target:
            return i-1
    return 0    
 
def addendfinder(rangetop):
    primes = findprimes(rangetop)
    evens = generate_evens(rangetop)
    print(primes)
    print(evens)
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
   
    
    
#    print(findprimes(50))
     firstaddend, secondaddend, eventarget = addendfinder(30)
     print("first addend:   " + str(firstaddend))
     print("second addend:  " + str(secondaddend))
     print("even target:  " + str(eventarget))
    
     plt.plot(eventarget, firstaddend, 'bs', eventarget, secondaddend,'g^')
     plt.ylabel('addends')
     plt.xlabel('even targets')
     plt.title("Goldbach")
    
    
    
    
     #print(generate_evens(22))
     
#    numlist = [9,8,7,6,5,4,3,2,1]
#    sortedlist = MergeSort(numlist)
#    hotindex = BinarySearch(sortedlist, 8)
#    gumlist = numlist[0:4]
#    print(numlist)
#    print(gumlist)

#print(checkforbiggerthan(sortedlist, 4))    
#    print("numlist     :" + str(numlist))
#    print("sortedlist  :" + str(sortedlist))
#    print("hotindex    :" + str(hotindex))
    
    
    
    
        