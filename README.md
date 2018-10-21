# MATHisFUN
Name: Rasul Silva (:

validate, visualize and explore mathematical concepts, proofs, and conjectures!

Here is a list of the projects contained in this repository with brief descriptions:

1. collatz.py - this is a visualization of the Collatz conjecture which is a repeated application of conditional calcultions to a starting value defined as shown below. The conjecture states that the sequence will reach 0 for any number. The plot displays the starting value on the x axis and the sequence length(the number of calculations required to get to 1) on the y axis.
               
               N/2        if N is even       
         N =                                   repeated application of these conditions to any number 
               3*N + 1    if N is odd          will produce 1 eventually (or so the conjecture states)                                                  
               
2.twinprimes.py - Here, we visualize the seemingly unpredictable nature of the twin prime distribution. For any given range (0 to rangetop), we calculate all of the twin prime pairs and show them on a plot as follows:
               
                   1 if twin prime
          F(x) =                          where x = the number in question
                   0 if not twin prime
                   

3. goldbach.py - Goldbach's conjecture states that any even integer above two is the sum of two primes. The output plot of the program displays ALL prime pairs that sum to any even target. For example, if our even target was 12, the 2 addends plotted would be 5 and 7. Unfortunately, the output does not seem to be particularly useful.    
                 

4. gilbreath.py - Gilbreath's conjecture states that if you take an ordered list of prime numbers and apply the forward difference operator to it (create a new list containing all the absolute differences between items in the original list) every generated list will start with a 1. Let's see an example to clarify!

                                       FDO             FDO            FDO          FDO        FDO
       prime_list = [2,3,5,7,11,13,...]->[1,2,2,4,2,...]->[1,0,2,2,...]->[1,2,0,...]->[1,2,...]->[1,...]
                                          ^                ^              ^            ^          ^
                               The first item in every generated list is 1
       This program will generate all Gilbreath lists for a prime list of all numbers up to the input value "prime_number_rangetop"
       and it will verify that they all start with a 1 (:
                
 
                   
