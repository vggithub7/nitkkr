import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder
#from sklearn.preprocessing import OneHotEncoder

#reading the dataset
df = pd.read_csv('/dataset/Data.csv')
df_x = df.iloc[:,0:3].values
df_y = df.iloc[:,3].values

#describing the dataset
df.describe()
#to display the dataset
display(df)

#insert missing values in column 2,3,4
imputer = SimpleImputer(missing_values = np.nan,strategy = 'mean')
df_x[:,1:4] = imputer.fit_transform(df_x[:,1:4])

#to check the inserted value
display(df_x)
# categorical to continous
country_encoder = LabelEncoder()
df_x[:,0] = country_encoder.fit_transform(df_x[:,0])
purchased_encoder = LabelEncoder()
df_y = purchased_encoder.fit_transform(df_y)

#to check the continues values
display(df_x)
display(df_y)
#print (sklearn.__version__)