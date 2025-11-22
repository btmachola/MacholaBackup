# -*- coding: utf-8 -*-
"""
Created on Thu Jul 31 10:12:28 2025

@author: B MACHOLA
"""

import matplotlib.pyplot as plt
import scipy

x= [1000,15000,20000,25000,30000,45000]
y=[152,191,245,299,362,390]

slope,intercept,r,p ,std_err = scipy.stats.linregress(x,y)

def mypred(x):
    return slope*x +intercept
yp=[]
for i in x:
    yp.append(mypred(i))
    
plt.scatter(x,y,color='r')
plt.plot(x,yp)