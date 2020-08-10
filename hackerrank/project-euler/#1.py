"""
Date: - 10-08-2020
Author: - SUSHIL SINGH
Problem : - #1: Multiples of 3 and 5
Question- Link: - https://www.hackerrank.com/contests/projecteuler/challenges/euler001/problem
"""

# solution
def SumDivisibleBy35(n,target):
    """
    Returns the sum of all the multiples of 3 or 5 below N
    """
    if target > 0:
        p = target // n
        return (n*(p*(p+1))) // 2
    else:
        return 0

if __name__ == "__main__":
    test = int(input())
    for _ in range(test):
        N = int(input()) 
        target = N-1
        print(SumDivisibleBy35(3,target) + SumDivisibleBy35(5,target) - SumDivisibleBy35(15,target))
        
      
