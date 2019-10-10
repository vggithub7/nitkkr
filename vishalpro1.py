#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 21:30:39 2018

@author: sunbeam
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# data cleaning

# read the datset
df = pd.read_csv('C:/Users/lab-9/Documents/Python lab/dataset/Data.csv')
print ("hello1")

print(df.median())
df_x = df.iloc[:,0:3].values
df_y = df.iloc[:,3].values

print ("printing df_x******************printing_df_x")
print(df_x)
print ("df_y******************")
print(df_y)
print("*******************************************************")

# remove NA values
from sklearn.impute import SimpleImputer
#from sklearn.preprocessing import Imputer
imputer = SimpleImputer(missing_values =np.nan,strategy = 'median')
df_x[:,1:4] = imputer.fit_transform(df_x[:,1:4])



plt.scatter(df_x,df_y)


print ("hello2_na's")

print ("printing df_x******************printing_df_x")
print(df_x)
print ("df_y******************")
print(df_y)
print("*******************************************************")

# categorical to continous
from sklearn.preprocessing import LabelEncoder
country_encoder = LabelEncoder()
df_x[:,0] = country_encoder.fit_transform(df_x[:,0])
purchased_encoder = LabelEncoder()
df_y = purchased_encoder.fit_transform(df_y)


print ("hello")

print ("printing df_x******************printing_df_x")
print(df_x)
print ("df_y******************")
print(df_y)
print("*******************************************************")

# add new columns





from sklearn.preprocessing import OneHotEncoder
hot_encoder = OneHotEncoder(categorical_features = [0])
df_x= hot_encoder.fit_transform(df_x).toarray()


print ("hello2")

print ("printing df_x******************printing_df_x")
print(df_x)
print ("df_y******************")
print(df_y)
print("*******************************************************")
plt.xlabel("aaaa")
plt.ylabel("abbbb")
model=LinearRegression().fit(df_x,df_y)
plt.scatter(df_x,model.predict(df_x),color='red')
#print(df)
#print(df)
#print(df)
#print(df)

# remove columns

# split the data into train and test

# perform the logic

# consume the result

# visualize the result
