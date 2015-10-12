class InitOusideCreate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def makeAttrOutside(self, z):
        self.z = z
    def printAttributes(self):
        try:
            print('x:%d ' % self.x),
            print('y:%d ' % self.y),
            print('z:%d ' % self.z),
        except AttributeError, e:
            print('\nAttributeError!')
            print(str(e))
        finally:
            print('')

obj1 = InitOusideCreate(1,2)
obj1.printAttributes()
obj1.makeAttrOutside(3)
obj1.printAttributes()
