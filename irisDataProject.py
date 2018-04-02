# Declan Barr 31 Mar 2018
# Iris Flower Data Set Project for Programming and Scripting
# Using numpy to determine mean
# https://www.dataquest.io/blog/numpy-cheat-sheet/
# Using pandas to read csv files https://www.kaggle.com/ashokdavas/iris-data-analysis-pandas-numpy
# https://github.com/pandas-dev/pandas/blob/master/doc/cheatsheet/Pandas_Cheat_Sheet.pdf
# Setting headers for datafile: https://towardsdatascience.com/pca-using-python-scikit-learn-e653f8989e60

import pandas as pd
import numpy as np

df = pd.read_csv('data/iris.csv', names=["Sepal Length", "Sepal Width", "Petal Length", "Petal Width", "Class"] ) 
print(df)
print(np.mean(df, axis=0)) # Axis = 0 means the columns, Axis = 1 means the rows
print("Rows 1 to 50 are:", df.iloc[0:50])
print("Rows 1 to 50 of Sepal length are:", df.iloc[0:50,[0]])
