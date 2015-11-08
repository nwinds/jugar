import math
def stdDevOfLengths(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
    if len(L) == 0:
        return float('NaN')
    lenList = [len(ele) for ele in L]
    avgLen = sum(lenList) / float(len(lenList))
    sd = math.sqrt(sum([(ele-avgLen)**2 for ele in lenList]) / float(len(L)))
    return sd
    #return round(sd, 4)
assert stdDevOfLengths(['a', 'z', 'p']) == 0.0
assert stdDevOfLengths(['apples', 'oranges', 'kiwis', 'pineapples']) == 1.8708
