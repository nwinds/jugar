def search3(L, e):
    print("List L: " + str(L))
    if L[0] == e:
        return True
    elif L[0] > e:
        return False
    else:
        return search3(L[1:], e)

#search3([], 4)
#search3([1, 2, 3], 4)

def search3M(L, e):
    print("List L: " + str(L))
    if L == []:
        return False
    if L[0] == e:
        return True
    elif L[0] > e:
        return False
    else:
        return search3M(L[1:], e)

search3M([], 4)
search3M([1, 2, 3], 4)