# -*- coding: utf-8 -*-
"""
Created on Sat Aug 23 13:36:56 2025

@author: B MACHOLA
"""


from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

from sklearn import linear_model

import numpy as np
import pandas as pd

N=100
df=pd.DataFrame(columns=['x1','x2','y','yl'])
df['x1']=1*np.random.normal(0,4,N)
df['x2']=1*np.random.normal(0,4,N)

df['y']=(df['x1']*2)/9 + (df['x2']*1)/1


df['yl']=0

for i in range(0,N):
    if df['y'][i]>1:
        df['yl'][i]=1
        
    if df['y'][i]**2>50:
        df['yl'][i]=2
        
        
df1=df[df['yl']==0]
df2=df[df['yl']==1]
df3=df[df['yl']==2]

x11=df1['x1']
x12=df1['x2']
y1=df1['y']
yl1=df1['yl']
plt.scatter(x11,x12,color='r')
x21=df2['x1']
x22=df2['x2']
y2=df2['y']
yl2=df2['yl']
plt.scatter(x21,x22,color='g')
x31=df3['x1']
x32=df3['x2']
y3=df3['y']
yl3=df3['yl']
plt.scatter(x31,x32,color='b')
plt.show()
