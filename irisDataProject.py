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
# print(df)
# print(np.mean(df, axis=0)) # Axis = 0 means the columns, Axis = 1 means the rows
# print("Rows 1 to 50 are:", df.iloc[0:50])
# print("Rows 1 to 50 of Sepal length are:", df.iloc[0:50,[0]])
# print("Mean of Sepal length for rows 1 to 50 is:", np.mean(df.iloc[0:50, [0]]))


# Attemping to create a loop that can cycle through classes - group of rows 0 to 49, 50 to 99 and 100 to 149
# and attributes - columns 0 to 3
"""
imin = 0
imax = 50
x = 0
print("The setosa rows are: ", df.iloc[imin:imax, [x]])

# This loop will print each of the attributes for each of the class of flowers
# Loop through flower classifications

for c in range(0, 3):
    print("class of flower: ", c)
    beginningRow = c * 50
    endRow = beginningRow + 50
# Loop through attributes
    for a in range(0, 4):
        print("Attribute is ", a)
        print("Data points are: \n")
        print(df.iloc[beginningRow:endRow, [a]])"""

# Function that goes through each attribute for each class of flower and passes
# a numpy argument aswell as the name
"""def attributefunc(arg, argname):
    # Loop through flower classifications
    for c in range(0, 3):
        beginningRow = c * 50
        endRow = beginningRow + 50
        print(df.iloc[beginningRow, [4]])
        # Loop through attributes
        for a in range(0, 4):
            print("The ", argname, "of attribute ", a," is ")
            print(arg(df.iloc[beginningRow:endRow, [a]]))

# Calculate the mean for each attribute of each class
attributefunc(np.mean, "mean")"""


print('{0:<9} {1:<14} {2:<13} {3:<14} {4:<13} '.format("Summary", "Sepal Length", "Sepal Width", "Petal length", "Petal Width"))
# This statement will format the return value of a function called minFunc
# The first arguement passed to minFunc will return the string "minimum"


# print('{a[o]} {a[1]} {a[2]} {a[3]} {a[4]}'.format(a=minFunc))


