#my own impl for merge sort, according to the sample tutorial
import operator
def merge(L1, L2, compare):
    merged = []
    i = 0
    j = 0
    while i < len(L1) and j < len(L2):
        if compare(L1[i], L2[j]):
            merged.append(L1[i])
            i += 1
        else:
            merged.append(L2[j])
            j += 1
    if i == len(L1):
        merged.extend(L2[j:])
    else:
        merged.extend(L1[i:])
    return merged

def mergeSort(L, compare = operator.lt):
    if len(L) < 2:
        return L[:]
    else:
        mid = len(L)//2
        left = mergeSort(L[:mid], compare)
        right = mergeSort(L[mid:], compare)
        return merge(left, right, compare)
        
def testMerge():
    print(merge([1,2,3,4,5], [6,7,8,9], operator.lt))
    print(merge([1,3],[2,4], operator.lt))    
    print(merge([],[1,2,3], operator.lt))
    print(merge([1,2,3],[], operator.lt))
    print(merge([],[], operator.lt))
    print(merge([1,2,3,4],[1,2,3], operator.lt))

#testMerge()
def testMergeSort():
    print(mergeSort([1,3,1,3,2]))

testMergeSort()
        