


## A Triangular series is a series of numbers where each number could be the row of an equilateral triangle.
## So 1,2,3,4,5 is a traingular series, because you could stack the numbers in equilateral triangle.
## Theire sum is 15, which makes 15 a traingular number


def sum_of_traingular_series(items):
    n = len(items)
    return (n*(n+1))/2
    

def find_n_of_traingular_series(sum):
    b, a, c = 1, 1, -2*sum
    D = pow(b,2) - 4*a*c
    
    res1 = (-b/2*a) + (math.sqrt(D)/2*a)
    res2 = (-b/2*a) - (math.sqrt(D)/2*a)
    
    if res1 < 0:
        return res1
    else:
        return res2
