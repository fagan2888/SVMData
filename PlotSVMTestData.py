# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 14:36:10 2013

@author: hok1
"""

import numpy as np
import pylab as pl

def extractSVMArffData(filename):
    data = np.loadtxt(filename, delimiter=',', skiprows=5,
                      dtype={'names': ('x1', 'x2', 'y'), 
                             'formats': (float, float, np.integer)})
    return data
    
def plotTwoClasses(data):
    isPositiveClass = lambda item: item[2]==1
    isNegativeClass = lambda item: item[2]==-1
    positiveData = filter(isPositiveClass, data)
    negativeData = filter(isNegativeClass, data)
    
    extract2D = lambda item: (item[0], item[1])
    
    positive2DData = np.transpose(map(extract2D, positiveData))
    negative2DData = np.transpose(map(extract2D, negativeData))
    
    pl.scatter(positive2DData[0], positive2DData[1], marker='o', c='r')
    pl.scatter(negative2DData[0], negative2DData[1], marker='D', c='b')
