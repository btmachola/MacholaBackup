# -*- coding: utf-8 -*-
"""
Created on Fri Aug  1 10:30:35 2025

@author: B MACHOLA
"""

import matplotlib.pyplot as plt
from sklearn import linear_model
import numpy as np
import pandas

df = pandas.DataFrame(columns=['x', 'y', 'yn'])

df['x1'] = np.ceil(np.random.normal(0, 10, 100))
df['x2'] = df['x1']**2
df['x3'] = df['x1']**3

df['y'] = df['x1']**3+ 6*df['x1']**2 + 11* df['x1']+6
df['yn'] = df['y']+ np.random.normal(0, 5, 100)

X = df[['x1','x2','x3']]
y= df['yn']

regr = linear_model.LinearRegression()
regr.fit(X, y)
print(regr.coef_)
#plt.plot(j,beta1)
#plt.show()