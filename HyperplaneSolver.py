# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 21:34:41 2013

@author: hok1
"""

import numpy as np

def getLinearSVMParameters(s1, s2, s3):
    slist = [list(s1), list(s2), list(s3)]
    for s in slist:
        s.append(1)
    stlist = map(np.array, slist)
        
    ylist = np.array([-1, 1, 1])
    Delta = np.matrix([[ylist[j] * np.dot(stlist[i], stlist[j]) for j in range(3)] for i in range(3)])
    alphaVec = np.linalg.inv(Delta)*(np.matrix(ylist).transpose())
    alphaVec = np.array(alphaVec)
    
    wt = np.array([0., 0., 0.])
    for i in range(3):
        wt += alphaVec[i]*ylist[i]*stlist[i]
    
    return (wt[:-1], wt[-1])

if __name__ == '__main__':
    s1 = np.array([-1, 0.])
    s2 = np.array([1., -1.])
    s3 = np.array([1., 1.])
    
    w, b = getLinearSVMParameters(s1, s2, s3)
    
    print 's1 = ', s1
    print 's2 = ', s2
    print 's3 = ', s3
    print 'w = ', w
    print 'b = ', b
