# -*- coding: utf-8 -*-
"""
Created on Tue Aug 26 10:18:45 2025

@author: B MACHOLA
"""

import numpy as np
#from sklearn import.datasets
from tensorflow import keras
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris

x, y = load_iris(return_X_y=True)
x_train, x_test,y_train, y_test=train_test_split(x,y,test_size=0.1, random_state=0)

model=keras.Sequential([keras.layers.Dense(100,input_shape=(4,),
activation='sigmoid'),keras.layers.Dense(3, activation='sigmoid')])
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy', metrics=['accuracy'])

model.fit(x_train,y_train,epochs=150) #150 iterations
model.evaluate(x_test,y_test)
y_pred=model.predict(x_test)
y_pred_l=[np.argmax(i) for i in y_pred]
print("Accuracy:", metrics.accuracy_score(y_test, y_pred_l))