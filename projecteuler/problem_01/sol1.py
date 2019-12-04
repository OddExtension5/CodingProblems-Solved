"""
Problem Statement:

If we list all the natural numbers below 20 that are multiples of 3 or 5,
we get 3,5,6,9,10,12,15,18. The sum if these multiples is 78.
Find the sum of all the multiples of 3 or 5 below N.

"""

def solution(n):
    """
    Return the sum of all the multiples of 3 or 5 below N

    >>> solution(3)
    0
    >>> solution(4)
    3
    >>> solution(10)
    23
    >>> solution(-7)
    0
    >>> solution(7000)
    11432168
    >>> solution(10000000000000000000000000000000000000000000000000000)
    Memory Error
    """

    return sum([m for m in range(3,n) if m % 3 == 0 or m % 5 == 0])

if __name__ == "__main__":
    print(solution(int(input().strip())))