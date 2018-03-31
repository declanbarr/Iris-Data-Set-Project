# Declan Barr 31 Mar 2018
# Iris Flower Data Set Project for Programming and Scripting
# Using numpy to read csv files and determine mean
# https://www.dataquest.io/blog/numpy-cheat-sheet/

import numpy as np
dataSet = np.genfromtxt('data/iris.csv',delimiter=',')

np.mean(dataSet, axis=0)
