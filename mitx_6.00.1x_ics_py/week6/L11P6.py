class Queue(object):
    def __init__(self):
        self.vals = []
    def insert(self, x):
        self.vals.append(x)
    def remove(self):
        if len(self.vals) != 0:
            return self.vals.pop(0)
        else:
            raise ValueError()
            