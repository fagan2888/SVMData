# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 17:29:11 2013

@author: hok1
"""

from numpy import random

class SVM2DDataGenerator:
    def __init__(self, a=1, b=1):
        """
        a : x-intercept
        b : y-intercept
        """
        self.a = a
        self.b = b
    
    def getClass(self, x1, x2):
        value = self.b*x1 + self.a*x2
        if (value >= self.a*self.b):
            return 1
        else:
            return -1
            
    def generateOneLine(self, x1, x2):
        classVal = self.getClass(x1, x2)
        return str(classVal)+' 1:'+str(x1)+' 2:'+str(x2)
    
    def generateFile(self, fileName, numData):
        file = open(fileName, 'wb')
        for i in range(numData):
            x1, x2 = 20 * random.rand(2) - 10
            file.write(self.generateOneLine(x1, x2)+'\n')
        file.close()
        
    def generateARFFOneLine(self, x1, x2):
        classVal = self.getClass(x1, x2)
        return str(x1)+", "+str(x2)+", "+str(classVal)
        
    def generateARFFFile(self, fileName, relationName, numData):
        file = open(fileName, 'wb')
        file.write('@relation \''+relationName+'\'\n')
        file.write('@attribute x1 NUMERIC\n')
        file.write('@attribute x2 NUMERIC\n')
        file.write('@attribute class {1, -1}\n')
        file.write('@data\n')
        for i in range(numData):
            x1, x2 = 20 * random.rand(2) - 10
            file.write(self.generateARFFOneLine(x1, x2)+'\n')
        file.close()
