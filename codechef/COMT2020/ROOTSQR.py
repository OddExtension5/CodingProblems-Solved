  
"""
Date: - 01-08-2020
Author: - SUSHIL SINGH
Problem : - Root & Square
Question- Link: - https://www.codechef.com/COMT2020/problems/ROOTSQR/
"""
# code
from math import sqrt

t, X = map(int, input().split())

for _ in range(t):
    N = int(input())
    if (N < 0):
        print("no")
    else:
        S = int(sqrt(N))
        con = 0.01*X*N
        diff = N - pow(S,2)
    
        if diff <= con:
            print("yes")
        else:
            print("no")
