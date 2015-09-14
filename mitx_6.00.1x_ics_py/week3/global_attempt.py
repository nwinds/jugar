def localVar():
    v = 10
    return v

def globalVar():
    global v
    v = -10
    return v


print('globalVar: %d' % globalVar())
global v
print('global v: %d' % v)
print('localVar: %d' % localVar())
print('global v: %d' % v)