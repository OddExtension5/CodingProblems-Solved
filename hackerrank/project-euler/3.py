"""
Date: - 10-08-2020
Author: - SUSHIL SINGH
Problem : - #3: Largest Prime Factor
Question- Link: - https://www.hackerrank.com/contests/projecteuler/challenges/euler003/problem
"""

# solution
import math 
  
def maxPrimeFactors(n): 
      
    # Initialize the maximum prime factor 
    # variable with the lowest one 
    maxPrime = -1
      
    # Print the number of 2s that divide n 
    while n % 2 == 0: 
        maxPrime = 2
        n >>= 1     # equivalent to n /= 2 
          
    # n must be odd at this point,  
    # thus skip the even numbers and  
    # iterate only for odd integers 
    for i in range(3, int(math.sqrt(n)) + 1, 2): 
        while n % i == 0: 
            maxPrime = i 
            n = n / i 
      
    # This condition is to handle the  
    # case when n is a prime number  
    # greater than 2 
    if n > 2: 
        maxPrime = n 
      
    return int(maxPrime) 
  
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(maxPrimeFactors(n))
        
