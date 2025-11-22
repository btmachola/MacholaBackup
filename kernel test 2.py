# -*- coding: utf-8 -*-
"""
Created on Sat Aug 23 13:26:45 2025

@author: B MACHOLA
"""

import pandas as pd
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn import metrics

df1=pd.read_csv('Mobile_Factory_train.csv')

MD1 = df1.keys()[0:19]

X=df1[MD1]
y=df1['price_range']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=0) 
clf = svm.SVC(kernel='linear')

clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)

print("Accuracy:",metrics.accuracy_score(y_test, y_pred))
