#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 12:01:39 2018

@author: amitk
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# data cleaning

# read the dataset
df = pd.read_csv('/Volumes/Data/Sunbeam/2018/August/DBDA/dataset/Wine.csv')
df_x = df.iloc[:, 0:13].values
df_y = df.iloc[:, 13].values


# remove NA values

# categorical to contineous

# add new columns

# remove columns


# scale the features 
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
df_x = scaler.fit_transform(df_x)

# split the data into train and test
from sklearn.cross_validation import train_test_split
x_train, x_test, y_train, y_test = train_test_split(df_x, df_y, train_size = 0.8, random_state = 0)

# scale the features 
#from sklearn.preprocessing import StandardScaler
#scaler = StandardScaler()
#x_train = scaler.fit_transform(x_train)
#x_test = scaler.fit_transform(x_test)

# apply pca
from sklearn.decomposition import PCA
pca = PCA(n_components=2)

# replace the train set with newly added columns
x_train = pca.fit_transform(x_train)

# replace the test set with newly added columns
x_test = pca.fit_transform(x_test)

# use svc
from sklearn.svm import SVC
classifier = SVC()
classifier = classifier.fit(x_train, y_train)
prediction = classifier.predict(x_test)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, prediction)

colors = ('red', 'green', 'blue')
for (index, value) in enumerate(np.unique(y_test)):
    plt.scatter(x_test[prediction == value, 0], x_test[prediction == value, 1], c = colors[index])






















