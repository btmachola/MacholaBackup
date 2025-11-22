# -*- coding: utf-8 -*-
"""
Created on Thu Aug 21 09:23:12 2025

@author: B MACHOLA
"""


from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn import neighbors

# Load digits dataset
digits = load_digits()

# Split dataset into train and test
x_train, x_test, y_train, y_test = train_test_split(
    digits.data, digits.target, test_size=0.1, random_state=0)

# Create KNN model (k=11)
model = neighbors.KNeighborsClassifier(n_neighbors=51)
model.fit(x_train, y_train)

# Manual accuracy calculation
count = 0
for i in range(x_test.shape[0]):
    y_pred = model.predict([x_test[i]])
    if y_pred == y_test[i]:
        count += 1

print("Score is:", count / x_test.shape[0])