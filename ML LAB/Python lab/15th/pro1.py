#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 19:50:09 2018

@author: sunbeam
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# data cleaning

# read the datset
df = pd.read_csv('/home/sunbeam/MLPractise/dataset/50_Startups.csv')
df_x = df.iloc[:,0:4].values
df_y =df.iloc[:,4].values
# remove NA values

# categorical to continous
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

state_encoder = LabelEncoder()
df_x[:,3] = state_encoder.fit_transform(df_x[:,3])
# add new columns
onehotencoder = OneHotEncoder(categorical_features=[3])
df_x  = onehotencoder.fit_transform(df_x).toarray() 
# remove columns

# split the data into train and test
from sklearn.cross_validation import train_test_split
x_train,x_test,y_train,y_test = train_test_split(df_x,df_y, train_size = 0.8)
# perform the logic
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor = regressor.fit(x_train,y_train)
result = regressor.predict(x_test)
# consume the result
result_1 = regressor.predict([[0,0,1,165349,136800,471700]])

# visualize the result