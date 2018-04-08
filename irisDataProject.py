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
print("Mean of Sepal length for rows 1 to 50 is:", np.mean(df.iloc[0:50, [0]]))


# Attemping to create a loop that can cycle through classes - group of rows 0 to 49, 50 to 99 and 100 to 149
# and attributes - columns 0 to 3
imin = 0
imax = 50
x = 0
print("The setosa rows are: ", df.iloc[imin:imax, [x]])