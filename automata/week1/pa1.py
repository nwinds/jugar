
"""
Question 2
The finite automaton below:
DFA with start state A and final state D. A has edge 0 to B and edge 1 to C; 
B has edge 1 to D; C has edge 0 to D; D has edge 0 to A and edge 1 to B.

accepts no word of length zero, no word of length one, and only two words of 
length two (01 and 10). There is a fairly simple recurrence equation for the 
number N(k) of words of length k that this automaton accepts. Discover this 
recurrence and demonstrate your understanding by identifying the correct value 
of N(k) for some particular k. Note: the recurrence does not have an 
easy-to-use closed form, so you will have to compute the first few values by 
hand. You do not have to compute N(k) for any k greater than 14.

"""
    
def initPossiabilities(k):
    probList = [i for i in range(0, 2**k)]
    return probList

# recursion helper
def transition(path, string):
    #start state
    if path == '':
        path = 'A'
    else:
        p = path[-1]
        if p == 'A':
            if string == 1:
                path += 'C'
            else:
                path += 'B'
        elif p == 'B':
            if string == 1:
                path += 'D'
        elif p == 'C':
            if string == 0:
                path += 'D'
        elif p == 'D':
            if string == 1:
                path += 'B'
            else:
                path += 'A'
    return path
    
# recursion process
def transPath(path, depth):
    if depth == 0:
        return 'A'
    else:
        return transition(transPath(path/2, depth-1), path%2)
        
def testTransPath():
    for depth in range(0, 4):
        for i in range(0, 2**depth):
            print('path[0x%x] = "%s"(%d)' % (i, transPath(i, depth), depth))
 

               
def allPaths(k):
    paths = []
    for i in range(0, 2**k):
        paths.append(transPath(i, k))
    return paths

def testAllPaths():
    print(allPaths(0))
    print(allPaths(1))
    print(allPaths(2))
    print(allPaths(3))


def countAccepted(probList, length):
    accepts = 0
    depth = length + 1
    for string in probList:
        if string[-1] == 'D' and len(string) == depth:
            accepts += 1
    return accepts

def testCountAccepted():
    probs0 = ['A']
    probs1 = ['AB', 'AC']
    probs2 = ['AB', 'ABD', 'ACD', 'AC']
    probs3 = ['AB', 'ABD', 'ABDA', 'ABDB', 'ACDA', 'ACDB', 'ACD', 'AC']
    print(countAccepted(probs0, 0))
    print(countAccepted(probs1, 1))
    print(countAccepted(probs2, 2))
    print(countAccepted(probs3, 3))

def N(k):
    probs = allPaths(k)
    print(countAccepted(probs, k))
    

# test 1: structure correctness
#print('---------------------')
#testTransPath() 
#print('---------------------')
#testAllPaths()
#print('---------------------')
#testCountAccepted()
    
#test 2: N(k) correctness test
#N(0)
#N(1)
#N(2)
#N(3)

#results
print('N(11) = '),
N(11)
print('N(12) = '),
N(12)
print('N(14) = '),
N(14)
#                                         