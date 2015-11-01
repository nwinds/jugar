import random
def deterministicNumber():
    '''
    Deterministically generates and returns an even number between 9 and 21
    '''
    random.seed()
    return 2 * random.randint(5, 10)
#deterministically!
