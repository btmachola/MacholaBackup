# -*- coding: utf-8 -*-
"""
Created on Wed Aug 13 10:45:39 2025

@author: B MACHOLA
"""

from sklearn.naive_bayes import GaussianNB
import numpy as np

x= ([2.7,0.6],[1.6,0.2],[2.9,0.7],[1.9,0.5],[2.3,0.8],[1.4,0.2],[1.7,0.3])
y= ([0,1,0,0,0,1,1])

mahesh = GaussianNB().fit(x,y)

z=np.array([[1.9,0.5],[1.32,0.29]])
print(mahesh.predict(z))
print(mahesh.predict_proba(z))