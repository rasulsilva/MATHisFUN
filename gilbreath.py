'''
Rasul Silva
DATE: 10/20/18
category: MATH FUN
Gilbreath validator

Description: Gilbreath's conjecture states that if you take a list of prime numbers
and apply to it the forward difference operator repeatedly, the first term in every 
generated list will be 1. See below
primes                 =   [2,3,5,7,11,13,...]
forward diff operator  =   [1,2,2,4,2,...]
forward diff again     =   [1,0,2,2,...]
                       =   [1,2,0,...]
                       =   [1,2,...]
                       =   [1,..]
Every generated list begins with a 1 for the list of ALL prime numbers
This program will generate these lists and validate that the starting value is a 1
for all prime numbers below the input "prime_number_rangetop"
'''
import math
import time

def is_prime(num):
    if num == 0 or num == 1: return False
    if num % 2 == 0: return False
    for value in range(2,int(num**.5) + 1):
        if num % value == 0:
            return False
    return True

def generate_prime_list(range_top):
    primes = [2]
    for i in range(2,range_top+1):
        if (is_prime(i)):
            primes.append(i)
    return primes    

def generate_diff_list(in_list):
    out_list = []
    for index in range(0,len(in_list)-1):
        diff = abs(in_list[index+1] - in_list[index])
        out_list.append(diff)
    return out_list

if __name__ == "__main__":

    prime_number_rangetop = 1000
    list_of_gilbreath_lists = []
    
    start = time.time()
    prime_list = generate_prime_list(prime_number_rangetop)
    end = time.time()
    print("duration: {}".format(end-start))
    prime_list_length = len(prime_list)
    print(prime_list)
    one_counter = 0
    temp_list = prime_list
    for step in range(0,prime_list_length-1):
        list_of_gilbreath_lists.append(temp_list)
        temp_list = generate_diff_list(temp_list)
        if (temp_list[0] == 1):
            one_counter = one_counter + 1
    

        
    print("with a range top of {} our prime number list is {} items long".format(prime_number_rangetop,prime_list_length))
    print("we see {} sequential lists that start with a 1".format(one_counter))
            
    
      
    
        

