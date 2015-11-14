from abc import ABCMeta
class MyABC:
    __metaclass__ = ABCMeta
MyABC.register(tuple)
assert issubclass(tuple, MyABC)
assert isinstance((), MyABC)

import abc
class Foo(object):
    #def __init__(self):
        #self.lst = [1,2,3]
    def __getitem__(self, index):
        #return self.lst[index]
        pass
    def __len__(self):
        pass
        #return len(self.lst)
    def get_iterator(self):
        return iter(self)



class MyIterable:
    __metaclass__ = ABCMeta

    @abc.abstractmethod
    def __iter__(self):
        while False:
            yield None

    def get_iterator(self):
        return self.__iter__()

    @classmethod
    def __subclasshook__(cls, C):
        if cls is MyIterable:
            if any("__iter__" in B.__dict__ for B in C.__mro__):
                return True
        return NotImplemented

MyIterable.register(Foo)