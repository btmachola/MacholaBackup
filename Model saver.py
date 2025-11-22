# -*- coding: utf-8 -*-
"""
Created on Thu Aug 28 09:15:49 2025

@author: B MACHOLA
"""

from tensorflow import keras
import numpy as np
from sklearn import metrics
from tensorflow.keras.models import load_model

# Load MNIST dataset
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

# Normalize the data
x_test = x_test / 255.0

# Flatten 28x28 images into 784 features
x_test_flattened = x_test.reshape(len(x_test), 784)

# Load pre-trained model
new_model = load_model('2ndDL.h5')

# Predict on test data
y_predicted = new_model.predict(x_test_flattened)

# Convert probabilities → class labels
y_predicted_labels = [np.argmax(i) for i in y_predicted]

# Print accuracy
print("Accuracy:", metrics.accuracy_score(y_test, y_predicted_labels))