def satisfiesF(L):
    """
    Assumes L is a list of strings
    Assume function f is already defined for you and it maps a string to a Boolean
    Mutates L such that it contains all of the strings, s, originally in L such
            that f(s) returns True, and no other elements. Remaining elements in L
            should be in the same order.
    Returns the length of L after mutation
    """
    # Your function implementation here
    #why the fuck is iterating original L while removing its elements may cause INCORRECT reply on oj?
    mirrL = L[:]
    for ele in mirrL:
        if f(ele) == False:
            L.remove(ele)
    return len(L)
        

#run_satisfiesF(L, satisfiesF)



print('-----------------------')
#test case 1
def f(s):
    return 'a' in s
L = ['a', 'b', 'a']
print satisfiesF(L)
print L

print('-----------------------')
#test case 2
L = []
print satisfiesF(L)
print L

print('-----------------------')
#test case 3
L = ['b']
print satisfiesF(L)
print L

print('-----------------------')
#test case 4
def f(s):
    return 'a' not in s
L = ['a', 'b', 'a']
print satisfiesF(L)
print L

print('-----------------------')
#test case 5
def f(s):
    return 'a' in s
L = ['a', 'b', 'a', 'b', 'c', 'd', 'a']
print satisfiesF(L)
print L