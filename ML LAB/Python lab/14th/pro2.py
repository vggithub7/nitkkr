#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 19:37:01 2018

@author: sunbeam
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# data cleaning

# read the datset
df= pd.read_csv('/home/sunbeam/MLPractise/dataset/Salary_Data.csv')
df_x= df.iloc[:,-1:].values
df_y = df.iloc[:,1].values
# remove NA values

# categorical to continous

# add new columns

# remove columns

# split the data into train and test
from sklearn.cross_validation import train_test_split
x_train,x_test,y_train,y_test = train_test_split(df_x,df_y,train_size = 0.8)
# perform the logic
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor = regressor.fit(x_train,y_train)
prediction = regressor.predict(x_test)
# consume the result
result = regressor.predict(5)
print(result)
# visualize the result
plt.scatter(df_x,df_y)
plt.plot(df_x,regressor.predict(df_x))
