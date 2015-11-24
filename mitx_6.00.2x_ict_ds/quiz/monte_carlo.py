

import random

def drawing_without_replacement_sim(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    4 red and 4 green balls. Balls are not replaced once
    drawn. Returns a float - the fraction of times 3 
    balls of the same color were drawn in the first 3 draws.
    '''
    ballColorSame = 0
    
    for n in range(numTrials):
        ballsDrawn = []
        choices = [0 for i in range(4)] + [1 for i in range(4)]
        for i in range(3):
            index = random.randrange(0, len(choices))
            ballsDrawn.append(choices.pop(index))
            #ballsDrawn.append(random.choice(choices))
        if sum(ballsDrawn) == 0 or sum(ballsDrawn) == 3:
            ballColorSame += 1
    return float(ballColorSame)/numTrials
   
import pylab
def drawPlot(lst):
    pylab.plot(lst, label = 'Monte Carlo simulation')
    pylab.title('Drawing 3 ball out of eight simulation')
    #pylab.xlabel('Time Steps')
    #pylab.ylabel('Average Virus Population')
    #pylab.legend(['virus population'])
    pylab.show()     

drawPlot([drawing_without_replacement_sim(100) for i in range(100000)])