# -*- coding: UTF-8 -*-
class Person:
    #name = ""
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return self.name
    def copy(self):
        return Person(self.name)

def deepCopy(x):
    if type(x) == type([]):
        return [deepCopy(x) for x in x]
    elif hasattr(x, 'copy'):
        return x.copy()
    else:
        return x

def deepMap(x, f):
    if type(x) == type([]):
        return [deepMap(x, f) for x in x]
    else:
        return f(x)

def deepPrint(x):
  print deepMap(x, lambda x: x.name if hasattr(x, 'name') else x)

#DEMO
list1 = [1, Person("fuxiang"), Person("muyu"), [Person("muyu")]]
list2 = deepCopy(list1)
list1[1].name = "muyu"

deepPrint(list1)
deepPrint(list2)