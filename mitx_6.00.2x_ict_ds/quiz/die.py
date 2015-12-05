import random
import pylab

# You are given this function
def getMeanAndStd(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    std = (tot/len(X))**0.5
    return mean, std

# You are given this class
class Die(object):
    def __init__(self, valList):
        """ valList is not empty """
        self.possibleVals = valList[:]
    def roll(self):
        return random.choice(self.possibleVals)

# Implement this -- Coding Part 1 of 2
def makeHistogram(values, numBins, xLabel, yLabel, title=None):
    """
      - values, a sequence of numbers
      - numBins, a positive int
      - xLabel, yLabel, title, are strings
      - Produces a histogram of values with numBins bins and the indicated labels
        for the x and y axis
      - If title is provided by caller, puts that title on the figure and otherwise
        does not title the figure
    """
    pylab.hist(values, bins=numBins)
    if title:
        pylab.title(title)
    pylab.xlabel(xLabel)
    pylab.ylabel(yLabel)
    pylab.show()
    
                    
# Implement this -- Coding Part 2 of 2
def getMaxSubstring(lst):
    #s = ''.join(lst)
    prev = 0
    start = 0
    end = 0
    runs = []
    for i in range(len(lst)):
        if lst[i] == prev:
            end += 1
        else:
            if end-start > 0: # not the begining case
                runs.append(end - start)
            start = i
            end = start + 1
        prev = lst[i]
    runs.sort()
    return runs[-1]

#assert getMaxSubstring([1,4,3]) == 1
#assert getMaxSubstring([1,3,3,2]) == 2
#assert getMaxSubstring([5,4,4,4,5,5,2,5]) == 3

def getAverage(die, numRolls, numTrials):
    """
      - die, a Die
      - numRolls, numTrials, are positive ints
      - Calculates the expected mean value of the longest run of a number
        over numTrials runs of numRolls rolls
      - Calls makeHistogram to produce a histogram of the longest runs for all
        the trials. There should be 10 bins in the histogram
      - Choose appropriate labels for the x and y axes.
      - Returns the mean calculated
    """        
    values = []
    for t in range(numTrials):
        dieRolled = []
        for r in range(numRolls):
            dieRolled.append(die.roll())            
        maxRun = getMaxSubstring(dieRolled)
        values.append(maxRun)                        
    makeHistogram(values, 10, 'Number on Die', 'Number of rolled', title=None)
    return float(sum(values))/len(values)

# One test case
values = getAverage(Die([1,2,3,4,5,6,6,6,7]), 500, 10000)
