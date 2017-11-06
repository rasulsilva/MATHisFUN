# -*- coding: utf-8 -*-

'''
Rasul Silva
10/04/17
category: MATH FUN
Collatz conjecture exploration and visualization

Description: Collatz conjecture states the following, 
take any number (n) and repeatedly apply the following formulas
if even: n = n/2
if odd: n = 3n + 1
n will always reach 1

let's see! (:
'''
import matplotlib.pyplot as plt

#calculates collatz sequence length for each number in range
def Collatzcalculation(rangestart, rangeend):
    sequencelength = []#the number of calculations it takes to reach 1
    ivalues = [] #list of starting values
    for i in range (rangestart,rangeend+1):
        ivalues.append(i)#add starting values to list
        print("calculate sequence for: " + str(i))
        sequence = []#into this will append the result of each calculation
        m = i #i copy
        j=1 # incrementer
        sequence.append(m)
        while m != 1:
            if m%2 == 0:#even procedure
                m = m/2
                sequence.append(m)
                j += 1
            else:#odd procedure
                m = 3*m + 1
                sequence.append(m)
                j += 1
                
        #print(sequence)
        sequencelength.append(j)
        print("sequence length is " + str(j) + " for a starting value of " + str(i) + "\n")
    
    return sequence, sequencelength, ivalues

#find the maximum value and its corresponding index for any set
def findmax(intlist):
    maxval = 0 # the maximum number contained in the list
    specindex = 0 # the index of the maximum number
    for i,j in enumerate(intlist):
        if j>maxval:
            maxval = j  
            specindex = i
          
    return maxval, specindex
            
        
        
if __name__ == "__main__":
    sequence, sequencelength, ivalues = Collatzcalculation(1,1000)
    maxvalue,specialindex = findmax(sequencelength)
    print("the maximum amount of calculations is " 
          + str(maxvalue) + " for the starting value " + str(specialindex+1))
    print(ivalues)
    print(sequencelength)
    plt.plot(ivalues, sequencelength, 'ro')
    plt.ylabel('# of calculations')
    plt.xlabel('Starting Value')
    plt.title("Starting Value vs. # of calculations")
    
    '''
    note to self:
        We notice that for a large range (0-1000 or more) we see an interesting design 
        that implies there is some pattern to the conditional calculation process
        specified by the conjecture. We cannot prove the conjecture with a program because 
        we can't check an infinite amount of numbers, so a traditional proof is needed
    '''
    
    
  
    


          
        
    