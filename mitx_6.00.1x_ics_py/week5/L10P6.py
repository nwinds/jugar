#bubble sort
def mySort(L):
    print('Bubble sort')
    clear = False
    while not clear:
        clear = True
        for j in range(1, len(L)):
            if L[j-1] > L[j]:
                clear = False
                temp = L[j]
                L[j] = L[j-1]
                L[j-1] = temp
        print(L)
                
def newSort(L):
    print('select sort')
    for i in range(len(L) - 1):
        j=i+1
        while j < len(L):
            if L[i] > L[j]:
                temp = L[i]
                L[i] = L[j]
                L[j] = temp
            j += 1
        print(L)
                
mySort([9,8,7,6,5,4,3,2,1])
newSort([9,8,7,6,5,4,3,2,1])
