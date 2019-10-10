#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 23:26:21 2018

@author: sunbeam
"""

# implement SVM Classifier and Regressor
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# data cleaning

# read the datset
df = pd.read_csv('/home/sunbeam/MLPractise/dataset/Social_Network_Ads.csv')
df_x = df.iloc[:,0:4].values
df_y =df.iloc[:,4].values

# remove NA values

# categorical to continous

# add new columns

# remove columns
df_x = df_x[:,3:4]
# split the data into train and test
from sklearn.cross_validation import train_test_split
x_train,x_test,y_train,y_test = train_test_split(df_x, df_y, train_size = 0.8)
# perform the logic
from sklearn.svm import SVR
regressor = SVR()
regressor = regressor.fit(x_train,y_train)
result_re = regressor.predict(x_test)
result_final = []
#result_final.append(0)
for i in range(0,len(result_re)):
    if result_re[i] > 0.4:
        result_final.append(1)
    else:
        result_final.append(0)

result_final = np.asarray(result_final)
    
#print(result_re)
# consume the result

# visualize the result
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test,result_final)
print(cm)
