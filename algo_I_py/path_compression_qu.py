# inspired by union find demo
identity = []

for i in range(10):
    identity.append(i)

# root of number
#I made an understandable ver
def root(you):
    while identity[you] != you:
        dad = identity[you]
        oldman = identity[dad]
        identity[you] = oldman
        you = identity[you]
    # shorter:
    #while identity[you] != you:
        #identity[you] = identity[identity[you]]
        #you = identity[you]
    return you
  
def connected(a, b):
    ra = root(a)
    rb = root(b)
    return ra == rb


def union(a, b):
    ra = root(a)
    rb = root(b)
    if ra == rb:
        return    
    identity[ra] = rb

print(identity)


union(1,2)
union(3,4)
union(5,6)
union(7,8)
union(7,9)
union(2,8)
union(0,5)
union(1,9)

print(identity)
print('size of connected components: %d' % len(identity))




