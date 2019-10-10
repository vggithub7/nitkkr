#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 16:50:02 2018

@author: sunbeam
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# data cleaning

# read the datset
df = pd.read_csv('/home/sunbeam/MLPython/dataset/Data.csv')
df_x = df.iloc[:,0:3].values
df_y = df.iloc[:,3].values
# remove NA values
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values= 'NaN',strategy ='mean',axis=0)
df_x[:,1:3] = imputer.fit_transform(df_x[:,1:3])

# categorical to continous
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
country_encoder = LabelEncoder()
df_x[:,0] = country_encoder.fit_transform(df_x[:,0])
purchased_encoder = LabelEncoder()
df_y = purchased_encoder.fit_transform(df_y)


# add new columns
onehotencoder = OneHotEncoder(categorical_features =[0])
df_x = onehotencoder.fit_transform(df_x).toarray()

# remove columns

# split the data into train and test

# perform the logic

# consume the result

# visualize the result