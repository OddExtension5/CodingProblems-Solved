######################################################
## FIND A DUPLICATE
#############################################

"""
We have a list of integers, where:

1. The integers are in the range 1..n
2. The list has a length of n+1

It follows that our list has at least one integer which appears at least twice. But it may have several duplicates, and each duplicate may appear more than twice.

Write a function which finds an integer that appears more than once in our list. (If there are multiple duplicates, you only need to find one of them.)

We're going to run this function on our new, super-hip MacBook Pro With Retina Display™. Thing is, the damn thing came with the RAM soldered right to the motherboard, so we can't upgrade our RAM. So we need to optimize for space!
"""

## Solution

## Naive: O(n) Time and O(n) Space
def find_repeat(numbers):
    numbers_seen = set()
    for number in numbers:
        if number in numbers_seen:
            return number
        else:
            numbers_seen.add(number)
    
    # Whoops -- no duplicate
    raise Exception('no duplicate')
        
    
