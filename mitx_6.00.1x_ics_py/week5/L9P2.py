def program3(L):
    totalSum = 0 #1
    highestFound = None #1
    for x in L: #1
        totalSum += x

    for x in L:#1
        if highestFound == None:
            highestFound = x
        elif x > highestFound:
            highestFound = x

    return (totalSum, highestFound)#1