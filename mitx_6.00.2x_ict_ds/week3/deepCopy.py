#suppose only int/list/None included
def deepCopy(lst, ):
    newList = []
    for ele in lst:
        if type(ele) == list:
            