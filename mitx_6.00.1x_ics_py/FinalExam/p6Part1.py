# -*- coding: utf-8 -*-
class Frob(object):
    def __init__(self, name):
        self.name = name
        self.before = None
        self.after = None
    def setBefore(self, before):
        # example: a.setBefore(b) sets b before a
        self.before = before
    def setAfter(self, after):
        # example: a.setAfter(b) sets b after a
        self.after = after
    def getBefore(self):
        return self.before
    def getAfter(self):
        return self.after
    def myName(self):
        return self.name
    def __str__(self):
        currFrob = self
        string = ''
        while(currFrob):
            string += currFrob.myName() + ' '
            #print(' '),
            currFrob = currFrob.getAfter()
        string += '\n'
        return string
            
        
def insert(atMe, newFrob):
    """
    atMe: a Frob that is part of a doubly linked list
    newFrob:  a Frob with no links 
    This procedure appropriately inserts newFrob into the linked list that atMe is a part of.    
    """
    if atMe.myName() < newFrob.myName():
        after = atMe.getAfter()
        prev = atMe
        while after:
            if after.myName() > newFrob.myName(): 
                break
            prev = after
            after = after.getAfter()
        if after:#after is the nearest bigger one        
            newFrob.setAfter(after)
            after.setBefore(newFrob)
        prev.setAfter(newFrob)
        newFrob.setBefore(prev)
            
    else:
        prev = atMe.getBefore()
        after = atMe
        while prev:
            if prev.myName() < newFrob.myName():
                break
            after = prev
            prev = prev.getBefore()
        if prev:
            prev.setAfter(newFrob)
            newFrob.setBefore(prev)
        newFrob.setAfter(after)
        after.setBefore(newFrob)


eric = Frob('eric')
andrew = Frob('andrew')
ruth = Frob('ruth')
fred = Frob('fred')
martha = Frob('martha')

insert(eric, andrew)
insert(eric, ruth)
insert(eric, fred)
insert(ruth, martha)