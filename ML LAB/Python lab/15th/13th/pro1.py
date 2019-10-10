#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 17:00:52 2018

@author: sunbeam
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# data cleaning
df = pd.read_csv('/home/kaizen/Python lab/dataset/Salary_Data.csv')
#df = df.iloc[:].values
df_x = df.iloc[:,:-1].values
df_y = df.iloc[:,1].values
# read the datset


# remove NA values
##imputer = Imputer(missing_values= 'NaN',strategy ='mean',axis=0)
#df[:,0:1] = imputer.fit_transform(df[:,0:1])

# categorical to continous

# add new columns

# remove columns

# split the data into train and test
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test= train_test_split(df_x,df_y,train_size= 0.8)

#perform the logic create regressor
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor = regressor.fit(x_train, y_train)
predicted_values = regressor.predict(x_test) 

output=regressor.predict([[15]])
print(output)

# consume the result

# visualize the result