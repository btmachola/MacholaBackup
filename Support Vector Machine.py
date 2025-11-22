# -*- coding: utf-8 -*-
"""
Created on Sat Aug 23 12:49:03 2025

@author: B MACHOLA
"""

from sklearn import svm
import numpy as np
import matplotlib.pyplot as plt

'''X=[[0,0],[1,0],[-2,1],[1,1.4],[2,2],[2,3],[3,2],[3,3]]
y=[0,0,0,0,1,1,1,1]
model = svm.SVC(kernel='linear')
model.fit(X,y)
print(model.coef_)
print(model.intercept_)
w=model.coef_[0]
a= -w[0]/w[1]
b= model.intercept_[0]
xx=np.linspace(0,4)
yy= a*xx -b/w[1]
h0=plt.plot(xx,yy)
for i in range (0,8):
    if (y[i]==0):
        plt.scatter(X[i][0],X[i][1],color='g')
    else:
        plt.scatter(X[i],[0],X[i][1],color='r')
plt.show()
'''
X=[[0,0],[1,0],[-2,1],[1,1.4],[2,2],[2,3],[3,2],[3,3]]
y=[0,0,0,0,1,1,1,1]
model=svm.SVC(kernel='linear')
model.fit(X,y)
print(model.coef_)
print(model.intercept_)
w=model.coef_[0]
a=-w[0]/w[1]
b=model.intercept_[0]
xx=np.linspace(0,4)
yy=a*xx-b/w[1]
h0=plt.plot(xx,yy)
for i in range(0,8):
    if(y[i]==0):
        plt.scatter(X[i][0],X[i][1],color='g')
    else:
        plt.scatter(X[i][0],X[i][1],color='r')
plt.show()