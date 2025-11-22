# -*- coding: utf-8 -*-
"""
Created on Thu Aug 28 10:46:13 2025

@author: B MACHOLA
"""

import tensorflow  as tf
import numpy as np
import matplotlib.pyplot as plt
#from tensorflow.keras.models import datasets,layers,models
from tensorflow.keras import datasets, layers, models

(x_train, y_train), (x_test, y_test) = datasets.cifar10.load_data()

xtrain=x_train/255
x_test=x_test/255
cnn = models.Sequential([

layers.Conv2D(filters=32, kernel_size=(3,3), activation='relu', input_shape=(32,32,3)),
layers.MaxPooling2D((2,2)),

layers.Conv2D(filters=20, kernel_size=(3,3), activation='relu'),
layers.MaxPooling2D((2,2)),


    layers.Flatten(),
    layers.Dense(20, activation='relu'),
    layers.Dense(10, activation='softmax')
    ])

cnn.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
cnn.fit(x_train, y_train, epochs=10)

cnn.save("first_cnn.h5")
