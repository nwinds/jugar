# O(N)
def uniqueValues(aDict):
    '''
    aDict: a dictionary
    '''
    # Your code here
    aKeys = []
    values = {}
    for key in aDict.keys():
        value = aDict[key]
        if value not in values:
            aKeys.append(key)
            values[value] = key
        elif values[value] != None:
            #replace values[value]'s original key as a hole
            aKeys.remove(values[value])
            values[value] = None
        #if is a hole, simply go on thr prosedure
    return aKeys
    
def testUniqueValues():
    print(uniqueValues({1: 1, 2: 2, 3: 3}))
    print(uniqueValues({1: 1, 2: 1, 3: 1}))
    print(uniqueValues({1: 1}))
    print(uniqueValues({1: 1, 2: 1, 3: 3}))
    print(uniqueValues({2: 2, 3: 3, 4: 4}))
    print(uniqueValues({}))
    print(uniqueValues({2: 0, 3: 3, 6: 1}))
    print(uniqueValues({1: 1, 3: 2, 6: 0, 7: 0, 8: 4, 10: 0}))
    print(uniqueValues({0: 9, 1: 1, 2: 7, 3: 3, 5: 2, 6: 5, 7: 8, 9: 10, 10: 0}))
    print(uniqueValues({8: 3, 1: 3, 2: 2}))
    print(uniqueValues({2: 2, 5: 0, 7: 3}))
    print(uniqueValues({5: 1, 7: 1}))
    print(uniqueValues({0: 3, 1: 2, 2: 3, 3: 1, 4: 0, 6: 0, 7: 4, 8: 2, 9: 7, 10: 0}))
    print(uniqueValues({0: 2, 1: 3, 2: 0, 3: 6, 7: 2, 9: 3}))
    print(uniqueValues({8: 1, 0: 4, 1: 1, 5: 2, 9: 4}))
    
testUniqueValues()
    