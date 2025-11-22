# -*- coding: utf-8 -*-
"""
Created on Fri Aug 29 11:01:20 2025

@author: B MACHOLA
"""

import numpy as np
import cv2
from tensorflow.keras.models import load_model

# Flower label dictionary
flowers_labels_dict = {
    'roses': 0,
    'daisy': 1,
    'dandelion': 2,
    'sunflowers': 3,
    'tulips': 4
}

# Load and preprocess test image
X = []
img = cv2.imread("C:/Users/+B MACHOLA/testing225.jpg")  # test image path
resized_img = cv2.resize(img, (180, 180))  # resize to model's input size
img1 = resized_img / 255.0  # normalize

X.append(img1)
X = np.array(X)

# Load trained CNN model
model = load_model("mycnnf.h5")

# Predict class
prediction = np.argmax(model.predict(X))
print("Predicted class index:", prediction)

# (Optional) Get flower name
labels_reverse = {v: k for k, v in flowers_labels_dict.items()}
print("Predicted flower:", labels_reverse[prediction])