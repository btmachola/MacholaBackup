# -*- coding: utf-8 -*-
"""
Created on Fri Aug  1 08:55:17 2025

@author: B MACHOLA
"""

import matplotlib.pyplot as plt
from sklearn import linear_model
import numpy as np
import pandas as pd

df = pd.DataFrame(columns=['x1', 'x2', 'x3', 'y', 'yn1', 'yn2', 'yn3'])

df['x1'] = np.ceil(100 * np.random.normal(0, 1, 1000))
df['x2'] = np.ceil(200 * np.random.normal(0, 3, 1000))
df['x3'] = np.ceil(500 * np.random.normal(0, 2, 1000))

df['y'] = 23.1+13.4 * df['x1'] + 2.7 * df['x2'] + 9.8 * df['x3']

X = df[['x1', 'x2', 'x3']]
beta1=[]
j=[0,10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190]
for i in range(0,200,10):
    df['n'] = np.random.normal(0, 1, 1000)  
    df['n'] = i*df['n']
    df['yn1']=df['y']+df['n']
    y=df['yn1']
    regr = linear_model.LinearRegression()
    regr.fit(X, y)
    beta1.append(regr.coef_[0])
plt.plot(j,beta1)
plt.show()