# provided function
def semordnilapWrapper(str1, str2):
    # A single-length string cannot be semordnilap
    if len(str1) == 1 or len(str2) == 1:
        return False

    # Equal strings cannot be semordnilap
    if str1 == str2:
        return False

    return semordnilap(str1, str2)

#handout
def semordnilap(str1, str2):
    '''
    str1: a string
    str2: a string
    
    returns: True if str1 and str2 are semordnilap;
             False otherwise.
    '''
    # Your code here
    # the philosophy: compare the strings using one single charactor at one time
    # Just 5 line(have had a good attempt on it)
    
    # str1 and str2 must meet their end at the same time, 
    # otherwise they are different
    if str1 == '' or str2 == '':
        return str1 == str2
    elif str1[0] == str2[-1]:
        return semordnilap(str1[1:], str2[:-1])
    return False
    
semordnilapWrapper('live', 'evil')
