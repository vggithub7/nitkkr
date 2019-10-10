#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 22:52:21 2018

@author: sunbeam
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# data cleaning

# read the datset
df = pd.read_csv('/home/sunbeam/MLPractise/dataset/50_Startups.csv')
df_x= df.iloc[:,0:4].values
df_y = df.iloc[:,4].values
# remove NA values

# categorical to continous

# add new columns

# remove columns
df_x = df_x[:,0:3]


# split the data into train and test
from sklearn.cross_validation import train_test_split
train_x,test_x,train_y,test_y = train_test_split(df_x,df_y, train_size=0.8)
# perform the logic
from sklearn.ensemble import RandomForestRegressor
regressor_rf= RandomForestRegressor()
regressort_rf = regressor_rf.fit(train_x,train_y)
result = regressor_rf.predict(test_x)

print(result)

# consume the result

# visualize the result