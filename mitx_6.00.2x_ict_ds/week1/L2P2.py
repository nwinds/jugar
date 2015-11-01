import random
def genEven():
    '''
    Returns a random even number x, where 0 <= x < 100
    '''
    # based on theory Set Rand1 uniformed distributed on another set will be rand, and will be uniformed/non-uniformed like Rand1
    random.seed()
    return 2 * random.randint(0,49)

#missleading answers provided below(==//) - will be disgussed later
# There are many good answers to this problem, some easier than others :)
def genEven():
    return random.randrange(0, 100, 2)

def genEven():
    return random.choice(range(0, 100, 2))

def genEven():
    return int(random.random() * 50)*2

def genEven():
    return random.choice(range(0, 50))*2

#I myself have some doubt on it
"""
Prob(even) = 50/99, Prob(odd) = 49/99, 
'even' win the guess game(with 1/99 advantage)




"""
def genEven():
    x = random.randint(0, 98)
    while x % 2 != 0:
        x = random.randint(0, 98)
    return x