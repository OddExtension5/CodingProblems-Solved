"""
Problem Statement:

If we list all the natural number below 20 that are multiples of 3 or 5,
we get 3,5,6,9,10,12,15,18. The sum if these multiples is 78.
Find the sum of all the multiples of 3 or 5 below N.

"""

def solution(n,target):
    """
    Returns the sum of all the multiples of 3 or 5 below N

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
    >>> solution(100000000000000000000)
    2333333333333333333316666666666666666668
    >>> solution(7000000000000000000000000000000)
    11433333333333333333333333333332166666666666666666666666666668
    >>>
   """
    if target > 0:
        p = target // n
        return (n*(p*(p+1))) //2
    else:
        return 0

if __name__ == "__main__":
    N = int(input())
    m = N-1
    print(solution(3,m) + solution(5,m) - solution(15,m))
