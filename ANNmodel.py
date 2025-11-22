# -*- coding: utf-8 -*-
"""
Created on Tue Aug 26 11:14:50 2025

@author: B MACHOLA
"""

import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt
import numpy as np

(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

x_train=x_train/255
x_test=x_test/255

plt.matshow(x_test[0])
x_train_flattened=x_train.reshape(len(x_train), 784)
x_test_flattened=x_test.reshape(len(x_test), 784)

model=keras.Sequential([keras.layers.Dense(300, input_shape=(784,), 
                                           activation='sigmoid'),
                       keras.layers.Dense(200, activation='sigmoid'),
                        keras.layers.Dense(10, activation='sigmoid')])


model.compile(optimizer='adam', 
              loss='sparse_categorical_crossentropy', 
              metrics=['accuracy'])

model.fit(x_train_flattened, y_train, epochs=15)
model.evaluate(x_test_flattened, y_test)
y_predicted=model.predict(x_test_flattened)
y_predicted_labels=[np.argmax(i) for i in y_predicted]
cm1=tf.math.confusion_matrix(y_test, y_predicted_labels)

model.save('DL1_model.h5')