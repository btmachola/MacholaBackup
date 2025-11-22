# -*- coding: utf-8 -*-
"""
Created on Wed Aug  6 10:07:19 2025

@author: B MACHOLA
"""

import matplotlib.pyplot as plt
from sklearn import cluster
import numpy as np

#data points
X= np.array([[2,-1],[1,-2],[1,1],[-1,-2],[2,1],[2,5],[3,7],[1,3],[1,5],[-1,-1],[1,-4]])
#X = np.array([[2, -1], [1, -2], [1, 1], [1, -3], [1, 1],
 #            [1, 2], [2, 5], [3, 7],[1, 3], [5, -1], [1, -4]])

# Apply KMeans clustering
model = cluster.KMeans(n_clusters=3)
model.fit(X)

# Print cluster centers and labels
print(model.cluster_centers_)
print(model.labels_)

# Cluster 0
C1 = []
for i in range(0, X.shape[0]):
    if model.labels_[i] == 0:
        C1.append(X[i])

C1 = np.array(C1)
x1 = C1[:, 0]
y1 = C1[:, 1]
plt.scatter(x1, y1)

# Cluster 1
C2 = []
for i in range(0, X.shape[0]):
    if model.labels_[i] == 1:
        C2.append(X[i])

C2 = np.array(C2)
y2 = C2[:, 0]
z2 = C2[:, 1]
plt.scatter(y2, z2)


# Cluster 2
C3 = []
for i in range(0, X.shape[0]):
    if model.labels_[i] == 2:
        C3.append(X[i])

C3 = np.array(C3)
y4 = C3[:, 0]
z4 = C3[:, 1]
plt.scatter(y4, z4)

# Plot cluster centers
CC = model.cluster_centers_
CC = np.array(CC)
y3 = CC[:, 0]
z3 = CC[:, 1]
plt.scatter(y3, z3, marker='*', s=200)

# Show plot
plt.show()