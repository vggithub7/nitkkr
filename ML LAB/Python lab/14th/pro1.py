#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 18:10:38 2018

@author: sunbeam
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# data cleaning

# read the datset
df = pd.read_csv('/home/kaizen/Python lab/dataset/50_Startups.csv')
df_x = df.iloc[:,0:4].values
df_y = df.iloc[:,4].values
# remove NA values

# categorical to continous

# add new columns

# remove columns
df_x= df_x[:,0:3]

# split the data into train and test
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test =train_test_split(df_x,df_y,train_size=0.8) 
# perform the logic
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor = regressor.fit(x_train,y_train)
prediction = regressor.predict(x_test)
print(prediction)
# consume the result

# visualize the result
plt.plot(x = x_train[:, 0], y = y_train)
plt.scatter(x = x_train[:, 0], y = y_train)
