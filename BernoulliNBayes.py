# -*- coding: utf-8 -*-
"""
Created on Wed Aug 13 11:06:27 2025

@author: B MACHOLA
"""

from sklearn.naive_bayes import BernoulliNB
import numpy as np
from sklearn.metrics import accuracy_score

x= np.random.randint(2, size=(500,100))
y= np.random.randint(2, size=(500,1))

for i in range (0,500):
    if y[i]==1:
        x[i,10]=1
        x[i,20]=0
        x[i,30]=0
        x[i,40]=0
        
# Create test dataset
x_test = x[:50]
y_test = y[:50]

# Train Bernoulli Naive Bayes model
model = BernoulliNB().fit(x, y)

# Predict on test set
y_pred = model.predict(x_test)

# Calculate accuracy
score = accuracy_score(y_test, y_pred)
print(score)
