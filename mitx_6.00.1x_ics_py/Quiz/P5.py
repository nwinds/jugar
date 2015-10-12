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
        
def primesList(N):
    '''
    N: an integer
    '''
    # Your code here
    primes = []

    for i in range(2, N+1):
        isPrime = True
        for j in primes:
            if gcdRecur(i, j) != 1:
                isPrime = False
                break
        if isPrime:
            primes.append(i)
    return primes
            
            