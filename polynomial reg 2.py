# -*- coding: utf-8 -*-
"""
Created on Fri Aug  1 11:08:14 2025

@author: B MACHOLA
"""

import matplotlib.pyplot as plt
from sklearn import linear_model
import numpy as np
import pandas as pd
import math

df = pd.DataFrame(columns=['x', 'y', 'yn'])

df=pd.read_csv("LRE1.csv")

X = df[['x1','x2','x3']]
y= df['yn']

regr = linear_model.LinearRegression()
regr.fit(X, y)
#print(regr.coef_)
plt.scatter(df['x1'],y)
plt.plot(df['x1'],y)
#plt.show()