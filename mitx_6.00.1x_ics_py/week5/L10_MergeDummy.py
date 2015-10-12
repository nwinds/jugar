#my own impl for merge sort, quit different from demo sample merge codes

def merge(L1, L2):
    merged = []
    i = 0
    j = 0
    while i < len(L1) and j < len(L2):
        if L1[i] <= L2[j]:
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
    
def testMerge():
    print(merge([1,2,3,4,5], [6,7,8,9]))
    print(merge([1,3],[2,4]))    
    print(merge([],[1,2,3]))
    print(merge([1,2,3],[]))
    print(merge([],[]))
    print(merge([1,2,3,4],[1,2,3]))

testMerge()
        