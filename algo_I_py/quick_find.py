# inspired by quick find demo
identity = []

for i in range(10):
    identity.append(i)

# find the id of belonged set
def find(i):
    return identity[i]
  
def connected(a, b):
    setid_a = find(a)
    setid_b = find(b)
    return setid_a == setid_b


def union(a, b):
    setid_a = find(a)
    setid_b = find(b) 
    if setid_a == setid_b:
        return
    for i in range(len(identity)):
        if identity[i] == setid_a:
            identity[i] = setid_b

print(identity)


union(2,1)

union(6,2)

union(3,0)

union(9,1)

union(4,2)
union(3,8)

print(identity)
print('size of connected components: %d' % len(identity))




