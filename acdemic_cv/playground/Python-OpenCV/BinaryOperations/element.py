# -*- coding: utf-8 -*-
import numpy as np

class element(object):
    def __init__(self, colsNum, rowsNum, anchorX, anchorY):
        self.colsNum = colsNum 
        self.rowsNum = rowsNum 
        self.anchorX = anchorX 
        self.anchorY = anchorY
        #initially black
        #testing
        self.block = np.array([(0,-1), (0,1)])

    def __str__(self):
        """Returns a string representation of self"""
        return 'element(%d, %d, %d, %d)' % \
        (self.colsNum, self.rowsNum, self.anchorX, self.anchorY)
        
    #helper
    def block(self):
        return self.block
        

