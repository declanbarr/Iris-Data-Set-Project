# Declan Barr 31 Mar 2018
# Iris Flower Data Set Project for Programming and Scripting
# Using numpy to read csv files and determine mean
# https://www.dataquest.io/blog/numpy-cheat-sheet/
# Using pandas to read csv files https://www.kaggle.com/ashokdavas/iris-data-analysis-pandas-numpy

import pandas as pd
import numpy as np

dataSet = pd.read_csv('data/iris.csv')

print(dataSet)
print(np.mean(dataSet, axis=0))
