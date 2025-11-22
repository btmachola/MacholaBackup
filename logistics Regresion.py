# -*- coding: utf-8 -*-
"""
Created on Sat Aug  2 09:59:09 2025

@author: B MACHOLA
"""

from sklearn import linear_model
from sklearn.metrics import confusion_matrix

x=[[752,6,2,1],[683,8,3,1],[720,5,2,1],[830,4,0,0],[872,3,0,1],[554,15,5,3],[634,18,5,3],[745,12,4,2],
                                        [604,5,3,0],[899,5,2,0]]
y=[[0],[0],[0],[0],[0],[1],[1],[1],[0],[1]]

model= linear_model.LogisticRegression()
model.fit(x,y)
z=[[560,40,4,3],[825,6,1,1],[750,10,2,1]]

y_pred= model.predct(z)
p_pred=model.predict_proba(z)
score = model.score(x,y)
r= confusion_matrix(y, model.predict(x))