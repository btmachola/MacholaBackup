# -*- coding: utf-8 -*-
"""
Created on Thu Aug 21 09:05:44 2025

@author: B MACHOLA
"""

from sklearn import neighbors

X=[[3,5,8],[-4,1,8],[2,7,8],[3,7,11],[6,7,9],[1,-9,12],[-3,5,-8]]

y=[0,0,1,1,1,0,0]

model=neighbors.KNeighborsClassifier(n_neighbors=5)
model.fit(X,y)
print(model.predict([[-2,-3,-10]]))
print(model.predict_proba([[-2,-3,-10]]))
