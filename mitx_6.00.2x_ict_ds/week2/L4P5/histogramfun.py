import pylab

# You may have to change this path
WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of uppercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print "  ", len(wordList), "words loaded."
    return wordList
"""
my impl
"""

#set line width
pylab.rcParams['lines.linewidth'] = 6
#set font size for titles 
pylab.rcParams['axes.titlesize'] = 20
#set font size for labels on axes
pylab.rcParams['axes.labelsize'] = 20
#set size of numbers on x-axis
pylab.rcParams['xtick.major.size'] = 5
#set size of numbers on y-axis
pylab.rcParams['ytick.major.size'] = 5

"""
stdDev from provided sample codes
"""
def stdDev(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    return (tot/len(X))**0.5

"""
CV from ppt
"""
def CV(X):
    mean = sum(X)/float(len(X))
    try:
        return stdDev(X)/mean
    except ZeroDivisionError:
        return float('NaN') 


def countWords(wordList):
    vows = 'aeiou'
    vowNumsList = []
    for word in wordList:
        word = word.lower()
        vowNum = 0
        for i in range(5):
            vowNum += word.count(vows[i])
        vowNumsList.append(vowNum)
    return vowNumsList

def getStatistics(wordList):
    vowNumsList = countWords(wordList)
    mean = sum(vowNumsList)/len(vowNumsList)
    sd = stdDev(vowNumsList)
    cv = CV(vowNumsList)
    return (vowNumsList, mean, sd, cv)

def labelPlot(mean, sd, cv):
    pylab.xlabel('Fraction of Heads')
    pylab.ylabel('Number of Trials')
    xmin, xmax = pylab.xlim()
    ymin, ymax = pylab.ylim()
    #add a text box
    pylab.text(xmin + (xmax-xmin)*0.02, (ymax-ymin)/2,
               'Mean = ' + str(round(mean, 4))
               + '\nSD = ' + str(round(sd, 4))
               + '\nCV = ' + str(round(cv, 4)))

def makePlots(wordList, numBins):
    val1, mean1, sd1, cv1 = getStatistics(wordList)
    #forcing the x axis the same as previous one
    pylab.hist(val1, bins = numBins)## makes visually differences in different sd
    xmin,xmax = pylab.xlim()
    ymin,ymax = pylab.ylim()
    labelPlot(mean1, sd1, cv1)

def plotVowelProportionHistogram(wordList, numBins=15):
    """
    Plots a histogram of the proportion of vowels in each word in wordList
    using the specified number of bins in numBins
    """
    makePlots(wordList, numBins)
    pylab.show()


if __name__ == '__main__':
    wordList = loadWords()
    plotVowelProportionHistogram(wordList)
