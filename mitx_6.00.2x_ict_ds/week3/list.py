import copy



lst1 = [2]
lst2 = [3]
lst3 = [5]
lstlst1 = [lst1, lst2, lst3]



print('shallow copy test')
lst4 = lst1
print('lst1'),
print(lst1)
print('lst4'),
print(lst4)
assert lst4 == lst1
print('\tadd one element into lst1')
lst1.append(7)
print('\tmodified lst1'),
print(lst1)
print('\tcurrent lst4'),
print(lst4)
assert lst4 == lst1
print('')




#test list in list
#list in list test: expected: lstlst4 == lstlst1 in value
print('list in list copy using copy.copy() test')
lstlst4 = copy.copy(lstlst1)
print('show two list after lstlst4 = copy.copy(lstlst1) executed')
print('lstlst1'),
print(lstlst1)
print('lstlst4'),
print(lstlst4)
assert lstlst1 == lstlst4

#modify one list inside list'list
#expected, since lstlst2 just referencing the same pointer to lst1, lst2, etc as lstlst1 do, should be the same
print('\tmodify one element in one list in lstlst1')
lst1[0] = lst1[0]**2
print('\tmodified lstlst1'),
print(lstlst1)
print('\tcurrent lstlst4'),
print(lstlst4)
assert lstlst1 == lstlst4
print('')

print('\tadd one element into lstlst4')
print('add in lst4, note, lst1 and lst4 are all the same!')
lstlst4 += lst4
print('\tmodified lstlst1'),
print(lstlst1)
print('\tcurrent lstlst4'),
print(lstlst4)
assert lstlst1 != lstlst4
print('')








#test list in list
#list in list test: expected: lstlst2 == lstlst1 in value
print('list in list copy using [:] test')
lstlst2 = lstlst1[:]
print('show two list after lstlst2 = lstlst1[:] executed')
print('lstlst1'),
print(lstlst1)
print('lstlst2'),
print(lstlst2)
assert lstlst1 == lstlst2
#modify one list inside list'list
#expected, since lstlst2 just referencing the same pointer to lst1, lst2, etc as lstlst1 do, should be the same
print('\tmodify one element in one list in lstlst1')
lst1[0] = lst1[0]**2
print('\tmodified lstlst1'),
print(lstlst1)
print('\tcurrent lstlst2'),
print(lstlst2)
assert lstlst1 == lstlst2
print('')


#
#deep copy
print('deepcopy test')
lstlst3 = copy.deepcopy(lstlst1)
lst1[0] /= 2
print('modified lst1'),
print(lst1)
print('current lstlst1'),
print(lstlst1)
print('current lstlst3'),
print(lstlst3)
assert lstlst3 != lstlst1
