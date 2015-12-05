import random
def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    # Your code here
    results = []
    bucketbase = [0, 0, 0, 1, 1, 1]#0 representing red, and 1 green
    for i in range(numTrials):
        balls = 0
        bucket = bucketbase[:]
        for j in range(3):
            #assert len(bucket) > 0
            index = random.randrange(len(bucket))
            balls += bucket.pop(index) 
        results.append(1 if (balls == 3 or balls == 0) else 0) #1: same color; 0: diff
    return float(sum(results))/len(results)
        
            
for i in range(10):
    noReplacementSimulation(random.randrange(10))
   
