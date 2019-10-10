#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 21:30:39 2018

@author: sunbeam
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# data cleaning

# read the datset
df = pd.read_csv('/home/kaizen/Python lab/dataset/Data.csv')
df_x = df.iloc[:,0:3].values
df_y = df.iloc[:,3].values
# remove NA values
from sklearn.impute import SimpleImputer
#from sklearn.preprocessing import Imputer
imputer = SimpleImputer(missing_values =np.nan,strategy = 'mean')
df_x[:,1:4] = imputer.fit_transform(df_x[:,1:4])

# categorical to continous
from sklearn.preprocessing import LabelEncoder
country_encoder = LabelEncoder()
df_x[:,0] = country_encoder.fit_transform(df_x[:,0])
purchased_encoder = LabelEncoder()
df_y = purchased_encoder.fit_transform(df_y)
# add new columns
from sklearn.preprocessing import OneHotEncoder
hot_encoder = OneHotEncoder(categorical_features = [0])
df_x= hot_encoder.fit_transform(df_x).toarray()
# remove columns

# split the data into train and test

# perform the logic

# consume the result

# visualize the result