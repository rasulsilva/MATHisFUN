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
                 
                   
                   
