# -*- coding: utf-8 -*-
"""
Created on Thu Aug 21 09:54:57 2025

@author: B MACHOLA
"""

import numpy as np
import cv2
#import tensorflow as tf
import pathlib
from sklearn.model_selection import train_test_split
from sklearn import neighbors

data_dir = 'datasets/flower_photos'
data_dir = pathlib.Path(data_dir)

#count all images
image_count = len(list(data_dir.glob('*/*.jpg')))
print(image_count)

flowers_images_dict = {
    'roses': list(data_dir.glob('roses/*')),
    'daisy': list(data_dir.glob('daisy/*')),
    'dandelion': list(data_dir.glob('dandelion/*')),
    'sunflowers': list(data_dir.glob('sunflowers/*')),
    'tulips': list(data_dir.glob('tulips/*')),
}

flowers_labels_dict = {
    'roses': 0,
    'daisy': 1,
    'dandelion': 2,
    'sunflowers': 3,
    'tulips': 4,
}


X, y = [], []

for x, z in flowers_images_dict.items():
    for image in z:
        img = cv2.imread(str(image))
        #print(z)
        resized_img = cv2.resize(img,(180,180))
        resized_img = np.reshape(resized_img, 97200)
        X.append(resized_img)
        y.append(flowers_labels_dict[x])
        


X = np.array(X)
y = np.array(y)


X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

X_train_scaled = X_train / 255
X_test_scaled = X_test / 255

num_classes = 5

model = neighbors.KNeighborsClassifier(n_neighbors=11)
model.fit(X_train, y_train)

