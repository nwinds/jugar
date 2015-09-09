# bisection search for guessing number between [0, 100)
# thinking of a number xThinking

delta = 1
numGuesses = 0
low = 0
high = 100
ans = (low + high)/2
xFlag = ''


print('Please think of a number between 0 and 100!')
while ans < high:
    print('Is your secret number %d?' % ans)
    xFlag = raw_input('Enter \'h\' to indicate the guess is too high. ' +\
                    'Enter \'l\' to indicate the guess is too low. ' +\
                    'Enter \'c\' to indicate I guessed correctly. ')
 
    if xFlag == 'l':
        low = ans
        ans = (low + high) // 2
    elif xFlag == 'h':
        high = ans
        ans = (low + high) // 2        
    elif xFlag == 'c':
        print('Game over. Your secret number was: %d' % ans)
        break
    else:
        print('Sorry, I did not understand your input.')


