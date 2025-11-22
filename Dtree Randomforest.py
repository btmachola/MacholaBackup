# -*- coding: utf-8 -*-
"""
Created on Wed Aug 20 10:47:26 2025

@author: B MACHOLA
"""

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.metrics import mean_squared_error 

df=pd.read_csv('Housing_Price_Train.csv')
df1=pd.read_csv('Housing_Price_Train.csv')

MD1 = df.keys()[1:80]

DP=[]
for i in range(1,79):
    if type(df[MD1[i]][1])==str:
        DP.append(MD1[i])
df=df.drop(DP, axis=1)

df = df.dropna(axis=1)

MD2 = df.keys()[1:35]

X=df[MD2]
y=df['SalePrice']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

model = linear_model.LinearRegression()
model.fit(X_train, y_train) 

y_pred_LR=model.predict(X_test)

print(mean_squared_error(y_test,y_pred_LR))