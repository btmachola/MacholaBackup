# -*- coding: utf-8 -*-
"""
Created on Thu Jul 31 10:39:15 2025

@author: B MACHOLA
"""

from sklearn import linear_model
import pandas
import math
df = pandas.read_csv("cars.csv")
X=df[['Weight','Volume']]
y=df['CO2']

model = linear_model.LinearRegression()
model.fit(X,y)
e=y-model.predict(X)
error=0
for i in range(0,X.shape[0]):
    error=error+e[i]**2
    
print('the mean sqr error is', math.sqrt(error/X.shape[0]))
print(model.predict([[1000,1500]]))