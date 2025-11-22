# -*- coding: utf-8 -*-
"""
Created on Thu Jul 31 11:23:38 2025

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
df['y'] = 13.4 * df['x1'] + 2.7 * df['x2'] + 9.8 * df['x3']
df['yn1'] = df['y'] + np.random.normal(0, 10, 1000)
df['yn2'] = df['y'] + np.random.normal(0, 50, 1000)
df['yn3'] = df['y'] + np.random.normal(0, 100, 1000)

df.to_csv('LRE.csv')

X = df[['x1', 'x2', 'x3']]
y = df['yn1']

regr = linear_model.LinearRegression()
regr.fit(X, y)
print(regr.coef_)