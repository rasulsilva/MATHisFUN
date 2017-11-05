# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 10:50:03 2017

@author: rasul_000
"""
'''
Rasul Silva
category: MATH FUN
Collatz conjecture exploration and visualization

Description: Collatz conjecture states the following, 
take any number (n) and repeatedly apply the following formulas
if even: n = n/2
if odd: n = 3n + 1
n will always reach 1

let's see
'''
import matplotlib.pyplot as plt

def Collatzcalculation(rangestart, rangeend):
    sequencelength = []
    ivalues = []
    for i in range (rangestart,rangeend+1):
        ivalues.append(i)
        print("calculate sequence for: " + str(i))
        sequence = []
        m = i #i copy
        j=1 # incrementer
        sequence.append(m)
        while m != 1:
            if m%2 == 0:#even
                m = m/2
                sequence.append(m)
                j += 1
            else:#odd
                m = 3*m + 1
                sequence.append(m)
                j += 1
                
        print(sequence)
        sequencelength.append(j)
        print("sequence length is " + str(j) + " for a starting value of " + str(i) + "\n")
    
    return sequence, sequencelength, ivalues

def findmax(intlist):
    maxval = 0
    specindex = 0
    for i,j in enumerate(intlist):
        if j>maxval:
            maxval = j
            specindex = i
          
    return maxval, specindex
            
        
        
if __name__ == "__main__":
    sequence, sequencelength, ivalues = Collatzcalculation(1,10000)
    maxvalue,specialindex = findmax(sequencelength)
    print("the maximum amount of calculations is " 
          + str(maxvalue) + " for the starting value " + str(specialindex+1))
    print(ivalues)
    print(sequencelength)
    plt.plot(ivalues, sequencelength, 'ro')
    plt.ylabel('# of calculations')
    plt.xlabel('Starting Value')
    plt.title("Starting Value vs. # of calculations")
    
    
  
    


          
        
    