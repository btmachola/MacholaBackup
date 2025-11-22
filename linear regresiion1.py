# -*- coding: utf-8 -*-
"""
Created on Thu Jul 31 10:25:35 2025

@author: B MACHOLA
"""

import matplotlib.pyplot as plt
from sklearn import linear_model

X= [[2,7,9],[1,9,6],[2,11,13],[12,1,1]]
y=[61,45,72,25]
regr=linear_model.LinearRegression()
regr.fit(X,y)
