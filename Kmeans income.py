# -*- coding: utf-8 -*-
"""
Created on Wed Aug  6 10:48:35 2025

@author: B MACHOLA
"""

from sklearn.cluster import KMeans
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv('Income.csv')

# Apply KMeans clustering
km = KMeans(n_clusters=3)
labels = km.fit_predict(df[['Age', 'Income']])

# Assign cluster labels to the DataFrame
df['cluster'] = labels

# Print cluster centers
print(km.cluster_centers_)

# Split data by cluster
df1 = df[df.cluster == 0]
df2 = df[df.cluster == 1]
df3 = df[df.cluster == 2]

# Scatter plots for each cluster
plt.scatter(df1.Age, df1.Income, color='green')
plt.scatter(df2.Age, df2.Income, color='red')
plt.scatter(df3.Age, df3.Income, color='black')

# Plot cluster centers
plt.scatter(km.cluster_centers_[:, 0], km.cluster_centers_[:, 1],
            marker='*', label='centroid')

# Label axes and show legend
plt.xlabel('Age')
plt.ylabel('Income')
plt.legend()

# Show plot
plt.show()