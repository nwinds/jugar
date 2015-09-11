# Euclid Algorithm Topic
# Iterate version for bruce force
def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    low = min(a, b)
    high = max(a, b)
    g = low
    while g > 1:
        if low % g == 0 and high % g == 0:
            break
        else:
            g -= 1
    return g
