'''
Given a list of string and numbers, rotate the string by one position to the right if the sum of squares of digits of the corresponding number is even and roate it
twice to the left if the summ of the squares of the digits of the corresponding number is odd.

INPUT:
['S','U','S','h','i',1,2,'t']

OUTPUT:
['S', 'h', 'i', 1, 2, 't', 'S', 'U']

'''


def digits(s):
    numbers = []  # to store numbers from a list of alphanumeric
    
    for i in s:
        if i in [0,1,2,3,4,5,6,7,8,9]:
            numbers.append(i)
    
    return numbers


def squareSum(numbers):
    return sum([pow(i,2) for i in numbers])


def main(s):
    """
    >>> main(['S','U','S','h','i',1,2,'t'])
    ['S', 'h', 'i', 1, 2, 't', 'S', 'U']

    """
    p = digits(s)

    if squareSum(p) % 2 == 0: # to check given sum of numbers is even or odd
        return (list(s[-1] + s[:-1]))
    else:
        return (s[2:] + s[:2])



# import testmode for testing our function
from doctest import testmod

if __name__ == '__main__':
    testmod(name='main', verbose=True)