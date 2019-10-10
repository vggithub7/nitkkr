#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 09:03:48 2018

@author: amitk
KMeans Clustering
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# read the dataset
df = pd.read_csv('/Volumes/Data/Sunbeam/2018/August/DBDA/dataset/Mall_Customers.csv')
#df = df.iloc[:, [3, 4]].values
df = df.iloc[:, 3:5].values

# find the optimal number of clusters
from sklearn.cluster import KMeans
wcss = []
for k in range(1, 11):
    info = KMeans(n_clusters = k, max_iter = 100)
    info = info.fit(df)
    wcss.append(info.inertia_)
    
plt.plot(range(1, 11), wcss)

# optimal number of clusters = 5

# get the 5 clusters info
info = KMeans(n_clusters = 5, max_iter = 100)
cluster_info = info.fit_predict(df)

# categorize the records based on cluster
cluster_1 = df[cluster_info == 0, ]
cluster_2 = df[cluster_info == 1, ]
cluster_3 = df[cluster_info == 2, ]
cluster_4 = df[cluster_info == 3, ]
cluster_5 = df[cluster_info == 4, ]

# visualize the clusters
plt.scatter(cluster_1[:, 0], cluster_1[:, 1], c='red', label = 'cluster 1')
plt.scatter(cluster_2[:, 0], cluster_2[:, 1], c='green', label = 'cluster 2')
plt.scatter(cluster_3[:, 0], cluster_3[:, 1], c='blue', label = 'cluster 3')
plt.scatter(cluster_4[:, 0], cluster_4[:, 1], c='cyan', label = 'cluster 4')
plt.scatter(cluster_5[:, 0], cluster_5[:, 1], c='magenta', label = 'cluster 5')
plt.scatter(info.cluster_centers_[:, 0], info.cluster_centers_[:, 1], c='yellow', s = 300)
plt.xlabel('Annual Income')
plt.ylabel('Spending Score')
plt.legend()




















