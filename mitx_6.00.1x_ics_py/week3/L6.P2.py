"""
Write a procedure called oddTuples, which takes a tuple as input, and returns a 
new tuple as output, where every other element of the input tuple is copied, 
starting with the first one. So if test is the tuple ('I', 'am', 'a', 'test', 
'tuple'), then evaluating oddTuples on this input would return the tuple ('I', 
'a', 'tuple').
"""

def oddTuplesFool(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    # Your Code Here
    retTuple = ()
    cnt = 0
    for ele in aTup:
        if cnt % 2 == 0:
            retTuple = retTuple + (ele,)
        cnt += 1
    return retTuple
    
def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    # Your Code Here
    ret = ()
    i = 0
    while i < len(aTup):
        if i % 2 == 0:
            ret += (aTup[i],)
        i += 1
    return ret