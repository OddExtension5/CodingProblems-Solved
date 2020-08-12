## Problem:
## I have a list of n+1 numbers. Every number in the range 1..n appears once except for one number that appears twice.
## Write a program for finding the number that appers twice.

## Time Complexity: O(n)
## Space Complexity: O(1)

# solution
def find_repeat(numbers_list):
    if len(numbers_list) < 2:
        raise ValueError('Finding duplicate requires at least two numbers')
    
    n = len(numbers_list) - 1
    sum_without_duplicate = (n*n + n)/2
    
    actual_sum = sum(numbers_list)
    
    return actual_sum - sum_without_duplicate
    
    
