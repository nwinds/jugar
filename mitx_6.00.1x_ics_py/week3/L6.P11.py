def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    # Your Code Here
    valNumMax = 0
    keyBiggest = None # including the exception case
    for key in aDict.keys():
        length = len(aDict[key])
        if valNumMax <= length:
            valNumMax = length
            keyBiggest = key
    return keyBiggest