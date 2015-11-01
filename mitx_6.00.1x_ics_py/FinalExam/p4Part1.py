def getSublists(L, n):
    subLists = []
    for i in range(len(L)-n+1):
        subLists.append(L[i:i+n])
    return subLists
    
#assert getSublists([10, 4, 6, 8, 3, 4, 5, 7, 7, 2], 4) == [[10, 4, 6, 8], [4, 6, 8, 3], [6, 8, 3, 4], [8, 3, 4, 5], [3, 4, 5, 7], [4, 5, 7, 7], [5, 7, 7, 2]]
#print('SUCCESS-1')
#assert getSublists([1, 1, 1, 1, 4], 2) == [[1, 1], [1, 1], [1, 1], [1, 4]]
#print('SUCCESS-2')
#assert getSublists([1, 1, 1, 1, 4], 1) == [[1], [1], [1], [1], [4]]
#print('SUCCESS-3')
     
def isAccessOrder(L):
    if len(L) == 0 or len(L) == 1:
        return True
    prev = L[0]
    for ele in L[1:]:
        if ele < prev:
            return False
        else:
            prev = ele
    return True

def longestRun(L):
    if len(L) == 0:
        return 0
    elif len(L) == 1:
        return 1
    for i in range(len(L), 0, -1):
        subLists = getSublists(L, i)
        for lst in subLists:
            if isAccessOrder(lst):
                return len(lst)
    return 0
    
#assert longestRun([10, 4, 6, 8, 3, 4, 5, 7, 7, 2]) == 5
#assert longestRun([0]) == 1
#assert longestRun([1, 1, 1, 1, 1]) == 5
#longestRun([1, 1, 1, 1, 1])
assert longestRun([-10, -5, 0, 5, 10]) == 5
print('SUCCESS - longestRun')
