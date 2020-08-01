"""
Date: - 01-08-2020
Author: - SUSHIL SINGH
Problem : - Help the Teacher
Question- Link: - https://www.codechef.com/problems/HELPTECH
"""

# code
for _ in range(int(input())):
    n = int(input())
    data = []
    for i in range(n):
        data.append(list(map(str, input().split())))
    
    sums = 0
    for i in data:
        sums += int(i[2])
    
    avg = sums/n
    poor = []
    
    for i in data:
        if ( avg > int(i[2])):
            poor.append(i)
            
    poor.sort(key = lambda ans: int(ans[2]))
    
    for i in poor:
        print(*i)
