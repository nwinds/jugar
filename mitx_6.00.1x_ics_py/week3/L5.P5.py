# Euclid Algorithm
def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    # ignore the a <= b case
    if b == 0:
        return a
    else:
        return gcdRecur(b, a % b)

print(gcdRecur(3,2))
print(gcdRecur(43,2))
print(gcdRecur(91,10))