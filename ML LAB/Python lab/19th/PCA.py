#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 17:11:55 2018

@author: sunbeam
"""
#Implement PCA With Classifier
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# data cleaning

# read the datset
df = pd.read_csv('/home/sunbeam/MLPractise/dataset/Wine.csv')
df_x = df.iloc[:,0:13].values
df_y = df.iloc[:,13].values
# remove NA values
# Scale the data
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
df_x[:,0:13] = scaler.fit_transform(df_x[:,0:13])

# categorical to continous

# add new columns

# remove columns apply PCA

from sklearn.decomposition import PCA
pca = PCA(n_components = 2)
df_x = pca.fit_transform(df_x[:,0:13]) 

# split the data into train and test
from sklearn.cross_validation import train_test_split
x_train,x_test,y_train,y_test = train_test_split
# perform the logic Apply PCA


# consume the result

# visualize the result

