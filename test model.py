# -*- coding: utf-8 -*-
"""
Created on Fri Aug 29 09:45:52 2025

@author: B MACHOLA
"""

from tensorflow.keras import datasets, layers, models
from tensorflow.keras.models import load_models

(x_train, y_train), (x_test, y_test) = datasets.cifar10.load_data()

x_train=x_train/255
x_test=x_test/255

cnn_model=load_model("first_cnn.h5")


cnn_model.evaluate(x_train,y_train)