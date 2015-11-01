import random

# Code Sample A
mylist = []

for i in xrange(random.randint(1, 10)):
    random.seed(0)
    if random.randint(1, 10) > 3: #some certain number x will hit '>3' condition
        number = random.randint(1, 10)
        if number not in mylist:
            mylist.append(number)
print mylist

#even if xrange() generats a randomized list, the bucket is deterministic