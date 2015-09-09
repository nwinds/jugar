# From Lecture 4, How Environments Separate Variable Bindings

def square(x):
    return x*x

def twoPower(x,n):
    while n > 1:
        x = square(x)
        n = n/2
    return x

# implementation according to lecture 4.5
x = 5
n = 1
print(twoPower(2, 8))
