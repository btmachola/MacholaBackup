# -*- coding: utf-8 -*-
"""
Created on Sat Aug 23 13:10:10 2025

@author: B MACHOLA
"""

#import numpy as np
from sklearn import svm
#import tensorflow as tf
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_digits

digits = load_digits()
x_train, x_test, y_train,y_test=train_test_split(digits.data,
                    digits.target,test_size=0.2, random_state=0)

model=svm.SVC(kernel='linear')

model.fit(x_train,y_train)
y_pred=model.predict(x_test)
print('accuraccy', metrics.accuracy_score(y_test,y_pred))
