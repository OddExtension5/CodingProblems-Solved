"""
Date: - 01-08-2020
Author: - SUSHIL SINGH
Problem : - Equal Number
Question- Link: - https://www.codechef.com/COMT2020/problems/EQUALNUM
"""

t = int(input())
for _ in range(t):
    n1, n2 = input().split()
    n1 = n1.replace(',', '')
    n2 = n2.replace(',', '')
    
    if n1 == n2:
        print("equal")
    else:
        print("different")
