# -*- coding: utf-8 -*-
# problem set 1
# COUNTING VOWELS
"""
For problems such as these, do not include raw_input statements or 
define the variable s in any way. Our automated testing will provide 
a value of s for you - so the code you submit in the following box 
should assume s is already defined. If you are confused by this 
instruction, please review L4 Problems 10 and 11 before you begin 
this problem set.
"""

# global variavle
s = 'abcd'

"""
quiz 1

"""

# passed
def isVowel(char):
    return char.lower() in 'aeiou'

def countVowel(s):
    total = 0
    for ch in s:
        if isVowel(ch):
            total += 1
    print('Number of vowels: %d' % total)

countVowel(s)


"""
quiz 2

Assume s is a string of lower case characters.
Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your program should print
Number of times bob occurs is: 2
"""
# passed
def findSubStr(s, keyword, step):
    num = 0
    firstHit = 0
    i = 0
    length = len(s)
    while i < length:
        firstHit = s.find(keyword, i)
        #print(firstHit)
        if firstHit >= 0:
            num += 1
            i = firstHit + step
        else:
            break
    return num

total = findSubStr(s, 'bob', 2)
print('Number of times bob occurs is: %d' % total)
    

"""
quiz 3


Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters occur 
in alphabetical order. For example, if s = 'azcbobobegghakl', then your program 
should print

Longest substring in alphabetical order is: beggh
In the case of ties, print the first substring. For example, if s = 'abcbcd', 
then your program should print

Longest substring in alphabetical order is: abc
"""

# passed
# actually I think this way is too stupid(but I don't wanna go further now
def findAlphabet(s):
    length = len(s)
    alphabetSet = []
    i = 0
    while i < length:
        j = i
        alphabet = [s[j]]
        while j < length-1:
            if ord(s[j+1]) >= ord(s[j]):    # next char fits
                j += 1
                alphabet.append(s[j])
            else:    # no longer fits
                break
        alphabetStr = ''.join(alphabet)
        alphabetSet.append(alphabetStr)
        i = j + 1 
    alphabetSet.sort(key=len, reverse=True)
    return alphabetSet.pop(0)

print('Longest substring in alphabetical order is: ' + findAlphabet(s))

# test for findAlphabet
def testFindAlphabet():
    strList = [
    'chrdrgzlgybdezkmve', 'szdxxoevpkvkncdrkubabfpn', \
    'aunxpwjpmkmpcaqqnuxd', 'xsnmwuktddx', \
    'ttrjleciidmyexuxmhxhqe', 'kigucfqnnei', \
    'mhboznmat', 'abcdefghijklmnopqrstuvwxyz', \
    'wfhbtjwkyzcmpqirq', 'qaiqjkvcwhesigweueuhgzc', \
    'fxxdbjlitdhzkmdzcz', 'zyxwvutsrqponmlkjihgfedcba', \
    'gqttwiln', 'dmquorzhom', \
    'oommbhdaluqaplwjmhbphxa', 'rdstxxsiwsr', \
    'xenhafaf', 'rpozxmuqurmpm', \
    'xmcuqmsyybolju', 'lfavqdxoylceqwyvqq']
    print('Test for findAlphabet:')
    for s in strList:
        print('Longest substring in alphabetical order is: ' + findAlphabet(s))


testFindAlphabet()

