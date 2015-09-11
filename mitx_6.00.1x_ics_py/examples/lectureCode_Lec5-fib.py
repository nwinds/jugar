def fib(x):
    """assumes x an int >= 0
       returns Fibonacci of x"""
       # Base case:
       # Female(0) = 1, Female(1) = 1
       
    assert type(x) == int and x >= 0
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)
