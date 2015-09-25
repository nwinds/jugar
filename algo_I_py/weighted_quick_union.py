# inspired by union find improvement #1 demo
# weighting tech
identity = []
size = []
for i in range(10):
    identity.append(i)
    size.append(1)

# root of number
def root(a):
    while identity[a] != a:
        a = identity[a]
    return a
  
def connected(a, b):
    ra = root(a)
    rb = root(b)
    return ra == rb
    
def union(a, b):
    ra = root(a)
    rb = root(b)
    if ra == rb:
        return  
    if size[ra] < size[rb]:
        identity[ra] = rb
        size[rb] += size[ra]
    else: # size[ra] >= size[rb]:
        identity[rb] = ra
        size[ra] += size[rb]


def printSizeList(li):
    sz = []
    for i in range(10):
        sz.append(0)
    for ele in li:
        r = root(ele)
        sz[r] += 1
    print(sz)
    

print(identity)


union(4,2)
union(0,8)
union(1,5)
union(3,6)
union(4,8)
union(3,1)
union(1,9)
union(8,5)
union(5,7)

print(identity)
print('size of connected components: %d' % len(identity))




