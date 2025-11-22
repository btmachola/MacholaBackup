# -*- coding: utf-8 -*-
"""
Created on Wed Aug  6 11:05:04 2025

@author: B MACHOLA
"""

from sklearn import datasets
from sklearn.cluster import KMeans

digits= datasets.load_digits()
X=digits.data[1:200]

kmeans = KMeans(n_clusters=5).fit(X)
print(kmeans.labels_)
