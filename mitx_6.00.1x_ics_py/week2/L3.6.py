# lecture 3.2, slide 6

# Find the cube root of a perfect cube
x = int(raw_input('Enter an integer: '))
ans = 0
for ans in range(0,abs(x)+1): # modified abs(x) to abs(x)+1
    if ans**3 == abs(x):      # modified >= to ==(in access mode)
        break

if ans**3 != abs(x):
    print(str(x) + ' is not a perfect cube')
else:
    if x < 0:
        ans = -ans
    print('Cube root of ' + str(x) + ' is ' + str(ans))
