def recurMul(a, b):
    if b == 1:
        return a
    else:
        return a + recurMul(a, b-1)

    
recurMul(2.0, 3.0)