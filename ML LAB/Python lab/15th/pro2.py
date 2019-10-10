#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 20:18:18 2018

@author: sunbeam
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# data cleaning

# read the datset
df = pd.read_csv('/home/sunbeam/MLPractise/dataset/Position_Salaries.csv')
df_x = df.iloc[:,1:2].values
df_y = df.iloc[:,2].values

# remove NA values

# categorical to continous

# add new columns
from sklearn.preprocessing import PolynomialFeatures
features = PolynomialFeatures(degree =4)
df_x = features.fit_transform(df_x)
# remove columns
df_x = df_x[:,1:]

# split the data into train and test
from sklearn.cross_validation import train_test_split
x_train,x_test,y_train,y_test = train_test_split(df_x,df_y,train_size =0.8)
# perform the logic
from sklearn.linear_model import LinearRegression
regression = LinearRegression()
regression = regression.fit(x_train,y_train)
result = regression.predict(x_test)
print(result)

# consume the result


# visualize the result
plt.scatter(df_x,df_y)
plt.plot(x_train,regression.predict(x_test))
