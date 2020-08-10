"""
Date: - 10-08-2020
Author: - SUSHIL SINGH
Problem : - #2: Even Fibonacci Numbers
Question- Link: - https://www.hackerrank.com/contests/projecteuler/challenges/euler002/problem
"""

## Solution #1
def solution1(limit):
    sum, a, b = 0, 1, 1
    
    while b < limit:
        if b % 2 == 0:
            sum += b
        c = a+b
        a = b
        b = c
    return sum
    
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        limit = int(input())
        print(solution1(limit))
        

## Solution #2
## If you observe the Fibonacci Sequence more closely you'll see that the every third fibonacci number is even.

def solution2(limit):
    sum, a, b = 0, 1, 1
    c = a + b
    
    while c < limit:
        sum += c
        a = b + c
        b = c + a
        c = a + b
    return sum

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        limit = int(input())
        print(solution2(limit))
    
    
