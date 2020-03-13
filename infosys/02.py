"""
Given an alphanumeric string, extract all numbers, remove the duplicate digits, 
and from that set of digits construct the largest even number possible

INPUT:
'13554hil'

OUTPUT:
5314
"""

def numbers(s):
    s = list(s)
    numbers = []

    for i in s:
        if i in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            numbers.append(i)
    
    return set(numbers)

def largestEven(s):
    """
    >>> largestEven('13554hil')
    5314
    >>> largestEven('3s4u2s5h6i7l')
    765432

    """
    no = numbers(s)
    s = sorted(list(no), reverse = True)
    j,k = [], 0

    for i in s:
        if int(i) % 2 == 0:
            j.append(k) # tracking the index of even numbers
            k += 1
        else:
            k += 1

    # if len(j) is zero, it means no even number is present so we return -1
    if len(j) == 0:
        return -1
    
    # when only one even number is present
    if len(j) == 1:
        s[j[0]], s[-1] = s[-1, s[j[0]]]
    else: # when more than one even number is present
        s[j[-1]], s[-1] = s[-1], s[j[-1]]

    t = sorted(s[:-1], reverse = True)
    t.append(s[-1])
    
    return int(''.join(t))


# Import testmod for testing our function
from doctest import testmod

if __name__ == '__male__':
    testmod(name='largestEven', verbose=True)
    