#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 20:53:45 2018

@author: sunbeam
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# data cleaning

# read the datset
df = pd.read_csv('/home/sunbeam/MLPractise/dataset/Social_Network_Ads.csv')
df_x = df.iloc[:,2:4].values
df_y = df.iloc[:,4].values
# remove NA values

# categorical to continous

# add new columns

# remove columns

# split the data into train and test
from sklearn.cross_validation import  train_test_split
x_train,x_test,y_train,y_test = train_test_split(df_x,df_y,train_size =0.8)
# perform the logic
from sklearn.tree import  DecisionTreeRegressor
regressor_dt = DecisionTreeRegressor()
regresoor_dt = regressor_dt.fit(x_train,y_train)
prediction_dt = regressor_dt.predict(x_test)

# consume the result



# visualize the result
plt.scatter(x = df_x, y = df_y)
plt.plot(x = df_x[:3], y = regressor_dt.predict(x_train[:3]))
