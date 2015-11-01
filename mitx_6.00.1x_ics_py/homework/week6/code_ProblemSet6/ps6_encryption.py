# 6.00x Problem Set 6
#
# Part 1 - HAIL CAESAR!

import string
import random

WORDLIST_FILENAME = "words.txt"

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    inFile = open(WORDLIST_FILENAME, 'r')
    wordList = inFile.read().split()
    print "  ", len(wordList), "words loaded."
    return wordList

def isWord(wordList, word):
    """
    Determines if word is a valid word.

    wordList: list of words in the dictionary.
    word: a possible word.
    returns True if word is in wordList.

    Example:
    >>> isWord(wordList, 'bat') returns
    True
    >>> isWord(wordList, 'asdf') returns
    False
    """
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\\:;'<>?,./\"")
    return word in wordList

def randomWord(wordList):
    """
    Returns a random word.

    wordList: list of words  
    returns: a word from wordList at random
    """
    return random.choice(wordList)

def randomString(wordList, n):
    """
    Returns a string containing n random words from wordList

    wordList: list of words
    returns: a string of random words separated by spaces.
    """
    return " ".join([randomWord(wordList) for _ in range(n)])

def randomScrambled(wordList, n):
    """
    Generates a test string by generating an n-word random string
    and encrypting it with a sequence of random shifts.

    wordList: list of words
    n: number of random words to generate and scamble
    returns: a scrambled string of n random words

    NOTE:
    This function will ONLY work once you have completed your
    implementation of applyShifts!
    """
    s = randomString(wordList, n) + " "
    shifts = [(i, random.randint(0, 25)) for i in range(len(s)) if s[i-1] == ' ']
    return applyShifts(s, shifts)[:-1]

def getStoryString():
    """
    Returns a story in encrypted text.
    """
    return open("story.txt", "r").read()


# (end of helper code)
# -----------------------------------


#
# Problem 1: Encryption
#
def buildCoder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation, numbers and spaces.

    shift: 0 <= int < 26
    returns: dict
    """
    
    if type(shift) != int:
        raise ValueError
    keys = {}  #keys = {|<upper letter sub-dict> | <lower sub> |}
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    upper0 = ord('A')
    lower0 = ord('a')
    for s in upper:
        keys[s] = chr(upper0 + ((ord(s) - upper0 + shift) % 26))
    for s in lower:
        keys[s] = chr(lower0 + ((ord(s) - lower0 + shift) % 26))
    return keys

def applyCoder(text, coder):
    """
    Applies the coder to the text. Returns the encoded text.

    text: string
    coder: dict with mappings of characters to shifted characters
    returns: text after mapping coder chars to original text
    """
    #skip type checking(python doing type checking is a fuck(may swift? that may be awsom, anyway forget about it)
    #text => plaintext
    #coder => key
    cipher = ''
    for ch in text:
        encoded = coder.get(ch, None)
        if encoded != None:
            cipher += encoded
        else:  # char's ignored cases
            cipher += ch
    return cipher

def applyShift(text, shift):
    """
    Given a text, returns a new text Caesar shifted by the given shift
    offset. Lower case letters should remain lower case, upper case
    letters should remain upper case, and all other punctuation should
    stay as it is.

    text: string to apply the shift to
    shift: amount to shift the text (0 <= int < 26)
    returns: text after being shifted by specified amount.
    """
    return applyCoder(text, buildCoder(shift))

    
#
# Problem 2: Decryption
#
def findBestShift(wordList, text):
    """
    Finds a shift key that can decrypt the encoded text.

    text: string
    returns: 0 <= int < 26
    """
    ignored = string.punctuation
    textList = []
    for ch in text:
        if ch in ignored:
            textList.append(' ')
        else:
            textList.append(ch)
    text = ''.join(textList)
    
    cipherList = text.split(' ')
    inversedShift = {} #sized list
    maxCount = 0
    count = 0
    for shift in range(26):
        maxCount = max(maxCount, count)
        count = 0 # set back to zero
        for cipher in cipherList:
            msg = applyShift(cipher, shift)
            if isWord(wordList, msg):
                count += 1
        inversedShift[shift] = count
    
    #get key with maximum count
    for key, val in inversedShift.items():
        if val == maxCount:
            return key
            
    return -1  # odd: when simply raise an exception, good local and error in oj

def decryptStory():
    """
    Using the methods you created in this problem set,
    decrypt the story given by the function getStoryString().
    Use the functions getStoryString and loadWords to get the
    raw data you need.

    returns: string - story in plain text
    """
    wordList = loadWords()
    cipher = getStoryString()
    shift = findBestShift(wordList, cipher)
    return applyShift(cipher, shift)


#testers
def testBuildCoder():
    #mit provided test cases
    #actually should try 0, 10 at first
    #ignore the negative int cases
    print('buildCoder(3)')
    assert buildCoder(3) == {'A': 'D', 'C': 'F', 'B': 'E', 'E': 'H', 'D': 'G', 'G': 'J', 'F': 'I', 'I': 'L', 'H': 'K', 'K': 'N', 'J': 'M', 'M': 'P', 'L': 'O', 'O': 'R', 'N': 'Q', 'Q': 'T', 'P': 'S', 'S': 'V', 'R': 'U', 'U': 'X', 'T': 'W', 'W': 'Z', 'V': 'Y', 'Y': 'B', 'X': 'A', 'Z': 'C', 'a': 'd', 'c': 'f', 'b': 'e', 'e': 'h', 'd': 'g', 'g': 'j', 'f': 'i', 'i': 'l', 'h': 'k', 'k': 'n', 'j': 'm', 'm': 'p', 'l': 'o', 'o': 'r', 'n': 'q', 'q': 't', 'p': 's', 's': 'v', 'r': 'u', 'u': 'x', 't': 'w', 'w': 'z', 'v': 'y', 'y': 'b', 'x': 'a', 'z': 'c'}
    print('buildCoder(9)')
    assert buildCoder(9) == {'A': 'J', 'C': 'L', 'B': 'K', 'E': 'N', 'D': 'M', 'G': 'P', 'F': 'O', 'I': 'R', 'H': 'Q', 'K': 'T', 'J': 'S', 'M': 'V', 'L': 'U', 'O': 'X', 'N': 'W', 'Q': 'Z', 'P': 'Y', 'S': 'B', 'R': 'A', 'U': 'D', 'T': 'C', 'W': 'F', 'V': 'E', 'Y': 'H', 'X': 'G', 'Z': 'I', 'a': 'j', 'c': 'l', 'b': 'k', 'e': 'n', 'd': 'm', 'g': 'p', 'f': 'o', 'i': 'r', 'h': 'q', 'k': 't', 'j': 's', 'm': 'v', 'l': 'u', 'o': 'x', 'n': 'w', 'q': 'z', 'p': 'y', 's': 'b', 'r': 'a', 'u': 'd', 't': 'c', 'w': 'f', 'v': 'e', 'y': 'h', 'x': 'g', 'z': 'i'}
    print('test of buildCoder success!')

def testApplyCoder():
    print('applyCoder("Hello, world!", buildCoder(3))')
    assert applyCoder("Hello, world!", buildCoder(3)) == 'Khoor, zruog!'
    print('applyCoder("Khoor, zruog!", buildCoder(23))')
    assert applyCoder("Khoor, zruog!", buildCoder(23)) == 'Hello, world!'
    print('test of applyCoder success!')

def testApplyShift():
    print('applyShift(\'This is a test.\', 8)')
    assert applyShift('This is a test.', 8) == 'Bpqa qa i bmab.'
    print('applyShift(\'Bpqa qa i bmab.\', 18)')
    assert applyShift('Bpqa qa i bmab.', 18) == 'This is a test.'
    print('ApplyShift success!')


def testFindBestShift():
    s = applyShift('Hello, world!', 8)
    print(s)
    assert findBestShift(wordList, s) == 18
    print(applyShift(s, 18))
#
# Build data structures used for entire session and run encryption
#

if __name__ == '__main__':
    # To test findBestShift:
    wordList = loadWords()
    s = applyShift('Hello, world!', 8)
    bestShift = findBestShift(wordList, s)
    assert applyShift(s, bestShift) == 'Hello, world!'
    # To test decryptStory, comment the above four lines and uncomment this line:
    #    decryptStory()


