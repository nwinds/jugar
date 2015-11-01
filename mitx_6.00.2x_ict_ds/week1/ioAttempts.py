#https://docs.python.org/2/tutorial/inputoutput.html#methods-of-file-objects
#formating

print('str.rjust:')
for x in range(1,11):
    print(repr(x).rjust(2) + ' ' + repr(x*x).rjust(3)),
    print(repr(x*x*x).rjust(4))
    
print('')
print('str.format:')
print('code: print(\'{0:2d} {1:3d} {2:4d}\'.format(x, x*x, x*x*x))')
for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))
print('by comparisom')
print('code: print(\'{2:2d} {1:3d} {0:4d}\'.format(x, x*x, x*x*x))')
for x in range(1, 11):
    print('{2:2d} {1:3d} {0:4d}'.format(x, x*x, x*x*x))

    
"""
(Note that in the first example, one space between each column was added by the 
way print works: it always adds spaces between its arguments.)
"""

