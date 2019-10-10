#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 11:36:53 2018

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

# split the data into train and test
from sklearn.cross_validation import train_test_split
x_train, x_test, y_train, y_test = train_test_split(df_x, df_y, train_size = 0.8, random_state = 0)

# Scaling features

# perform the logic
from sklearn.svm import SVC
classifier = SVC()
classifier = classifier.fit(x_train, y_train)
prediction = classifier.predict(x_test)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, prediction)

# consume the result

# visualize the result
#plt.scatter(x_test[:, 12], x_test[:, 11], c = 'red')
#plt.scatter(x_test[prediction == 1, 0], x_test[prediction == 1, 1], c = 'red')
#plt.scatter(x_test[prediction == 2, 0], x_test[prediction == 2, 1], c = 'green')
#plt.scatter(x_test[prediction == 3, 0], x_test[prediction == 3, 1], c = 'blue')

colors = ('red', 'green', 'blue')
#for index in range(0, 3):
for (index, value) in enumerate(np.unique(y_test)):
    plt.scatter(x_test[prediction == value, 0], x_test[prediction == value, 1], c = colors[index])











