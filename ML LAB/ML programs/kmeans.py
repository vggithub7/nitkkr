#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 15:47:41 2018

@author: sunbeam
"""
#implement PCA and Kmeans
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# data cleaning

# read the datset
df = pd.read_csv('dataset/Mall_Customers.csv')
df = df.iloc[:,3:5].values
# remove NA values
print("hii")
print(df)
# categorical to continous

# add new columns

# remove columns#    
from sklearn.cluster import KMeans
wcss = []
for k in range(1, 11):
    info = KMeans()#(n_clusters = k, max_iter = 100)
    info = info.fit(df)
    wcss.append(info.inertia_)
#Finding the elbow Point    
#plt.plot(range(1, 11), wcss)

# split the data into train and test
#PErform the logic
info = KMeans(n_clusters = 6,max_iter = 100)
cluster_info = info.fit_predict(df)
  
# categorize the records based on cluster
cluster_1 = df[cluster_info == 0, ]
cluster_2 = df[cluster_info == 1, ]
cluster_3 = df[cluster_info == 2, ]
cluster_4 = df[cluster_info == 3, ]
cluster_5 = df[cluster_info == 4, ]
cluster_6 = df[cluster_info == 5, ]

# visualize the clusters
plt.scatter(cluster_1[:, 0], cluster_1[:, 1], c='red', label = 'cluster 1')
plt.scatter(cluster_2[:, 0], cluster_2[:, 1], c='green', label = 'cluster 2')
plt.scatter(cluster_3[:, 0], cluster_3[:, 1], c='blue', label = 'cluster 3')
plt.scatter(cluster_4[:, 0], cluster_4[:, 1], c='cyan', label = 'cluster 4')
plt.scatter(cluster_5[:, 0], cluster_5[:, 1], c='magenta', label = 'cluster 5')
plt.scatter(cluster_6[:, 0], cluster_6[:, 1], c='black', label = 'cluster 6')
#plt.scatter(info.cluster_centers_[:, 0], info.cluster_centers_[:, 1], c='yellow', s = 300)
plt.xlabel('Annual Income')
plt.ylabel('Spending Score')
plt.legend()
plt.show()


