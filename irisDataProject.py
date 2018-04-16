# Declan Barr 31 Mar 2018
# Iris Flower Data Set Project for Programming and Scripting
# Using pandas to read csv files https://www.kaggle.com/ashokdavas/iris-data-analysis-pandas-numpy
# https://github.com/pandas-dev/pandas/blob/master/doc/cheatsheet/Pandas_Cheat_Sheet.pdf
# Setting headers for datafile: https://towardsdatascience.com/pca-using-python-scikit-learn-e653f8989e60

import pandas as pd

df = pd.read_csv('data/iris.csv', names=["Sepal Length", "Sepal Width", "Petal Length", "Petal Width", "Class"] ) 

print(df.head(5))
print(df.tail(5))
print("Number of rows and columns: ", df.shape)

setosaSepalLength = df.iloc[0:50,[0]]
print(setosaSepalLength.min())
print(setosaSepalLength.max())
print(setosaSepalLength.mean())

print("Basic Statistics for entire dataset: ")
print(df.describe())

setosa = (df.iloc[0:50])
print("Basic statistics for Iris setosa: ")
print(setosa.describe())

versicolor = (df.iloc[50:100])
print("Basic statistics for Iris versicolor: ")
print(versicolor.describe())

virginica = (df.iloc[100:150])
print("Basic statistics for Iris virginica: ")
print(virginica.describe())

