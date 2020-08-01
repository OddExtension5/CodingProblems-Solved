  
"""
Date: - 01-08-2020
Author: - SUSHIL SINGH
Problem : - BHPORSRP
Question- Link: - https://www.codechef.com/COMT2020/problems/BHPORSRP
"""

# code
t = int(input())
for _ in range(t):
    s = input()
    s_low = s.lower()
    
    a = "berhampore"
    b = "serampore"
    
    if a in s_low and b in s_low:
        print("Both")
    elif a in s_low:
        print("GCETTB")
    elif b in s_low:
        print("GCETTS")
    else:
        print("Others")
    
