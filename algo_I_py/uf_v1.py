# sets merging
# and for l1.1 quiz
# stupid approach of quick find(same phylosophy
#simple and plain to understand, ignorring in implementing
numSet = []

def locate(ele):
    for i in range(len(numSet)):
        subSet = numSet[i]
        if ele in subSet:
            return i
    return -1 # exception case
  
def connected(a, b):
    ia = locate(a)
    if ia < 0:
        return False
    return b in numSet[ia]


def union(a, b):
    ia = locate(a)
    ib = locate(b)
    if ia < 0 and ib < 0:
        numSet.append([a, b])
    elif ia < 0:
        numSet[ib].append(a)
    elif ib < 0:
        numSet[ia].append(b)
    elif ia == ib:                  # both exists, same set
        return
    else:                           # both exists, different set
        tmp_b = numSet[ib][:]       # deep copy
        numSet[ia].extend(tmp_b)    # merge
        del numSet[ib]              # delete the old set inefficient       


for i in range(10):
    numSet.append([i])

print(numSet)


union(1,2)
union(3,4)
union(5,6)
union(7,8)
union(7,9)
union(2,8)
union(0,5)
union(1,9)

print(numSet)
print('size of connected components: %d' % len(numSet))




