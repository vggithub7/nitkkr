#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 11:39:42 2018

@author: amitk
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# read the dataset
df = pd.read_csv('/Volumes/Data/Sunbeam/2018/August/DBDA/dataset/Mall_Customers.csv')
#df = df.iloc[:, [3, 4]].values
df = df.iloc[:, 3:5].values

# optimal number of clusters
import scipy.cluster.hierarchy as sch
dendogram = sch.dendrogram(sch.linkage(df))
plt.show()

# optimal number of clusters = 5
# AgglomerativeClustering: Hiearchical using  Top-Bottom approach
from sklearn.cluster import AgglomerativeClustering
clustering = AgglomerativeClustering(n_clusters = 5, affinity = 'euclidean')
info = clustering.fit_predict(df)

# visualization
cluster_1 = df[info == 0, ]
cluster_2 = df[info == 1, ]
cluster_3 = df[info == 2, ]
cluster_4 = df[info == 3, ]
cluster_5 = df[info == 4, ]

plt.scatter(cluster_1[:, 0], cluster_1[:, 1], c='red', label='cluster1')
plt.scatter(cluster_2[:, 0], cluster_2[:, 1], c='green', label='cluster2')
plt.scatter(cluster_3[:, 0], cluster_3[:, 1], c='blue', label='cluster3')
plt.scatter(cluster_4[:, 0], cluster_4[:, 1], c='cyan', label='cluster4')
plt.scatter(cluster_5[:, 0], cluster_5[:, 1], c='magenta', label='cluster5')
plt.xlabel('Annual Income')
plt.ylabel('Spending Score')
plt.legend()


























