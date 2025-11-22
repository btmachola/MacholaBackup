# -*- coding: utf-8 -*-
"""
Created on Sat Aug  2 10:42:46 2025

@author: B MACHOLA
"""

from sklearn import datasets
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.metrics import confusion_matrix

digits = datasets.load_digits()
x_train,x_test,y_train,y_test=train_test_split(digits.data,
                                               digits.target,test_size=0.2, random_state=0)

model=linear_model.LogisticRegression()
model.fit(x_train,y_train)
predictions= model.predict(x_test)
score = model.score(x_test,y_test)
r= confusion_matrix(y_test, model.predict(x_test))