def f(x):
    import math
    return 10*math.e**(math.log(0.5)/5.27 * x)


epsilon = 0.001

def radiationExposure(start, stop, step):
    '''
    Computes and returns the amount of radiation exposed
    to between the start and stop times. Calls the 
    function f (defined for you in the grading script)
    to obtain the value of the function at any point.
 
    start: integer, the time at which exposure begins
    stop: integer, the time at which exposure ends
    step: float, the width of each rectangle. You can assume that
      the step size will always partition the space evenly.

    returns: float, the amount of radiation exposed to 
      between start and stop times.
    '''
    # FILL IN YOUR CODE HERE...
    #suppose start% step == 0 and stop % step == 0
    start = int(start)
    stop = int(stop)
    step = float(step)

    curr = start
    result = 0.0
    while abs(curr - stop) > epsilon:
        result += f(curr) * step
        
        curr += step
        print('result=%.10f\t<time - %.1f>' % (result, curr))
        
    #debug
    print('----< result >-----')

    return result


# test cases
print('-------------------')
print(radiationExposure(0, 5, 1))
print('-------------------')
print(radiationExposure(5, 11, 1))
print('-------------------')
print(radiationExposure(0, 11, 1))
print('-------------------')
print(radiationExposure(40, 100, 1.5))
print('-------------------')
