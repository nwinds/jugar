# inspired by union find demo
identity = []

for i in range(10):
    identity.append(i)

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
    identity[rb] = ra

print(identity)


union(6,7)
union(6,9)
union(0,8)


union(1,9)
union(2,3)
union(5,7)

union(8,2)
union(2,1)
union(7,4)
print(identity)
print('size of connected components: %d' % len(identity))




