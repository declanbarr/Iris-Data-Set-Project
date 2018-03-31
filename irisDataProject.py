# Declan Barr 31 Mar 2018
# Iris Flower Data Set Project for Programming and Scripting
# Using numpy to read csv files and determine mean
# https://www.dataquest.io/blog/numpy-cheat-sheet/
# Using pandas to read csv files https://www.kaggle.com/ashokdavas/iris-data-analysis-pandas-numpy
# https://github.com/pandas-dev/pandas/blob/master/doc/cheatsheet/Pandas_Cheat_Sheet.pdf

import pandas as pd
import numpy as np

# df1 = ['sepalLength', 'sepalWidth', 'petalLength', 'petalWidth', 'class']
#df2 = pd.read_csv('data/iris.csv')

# does this need a reference to https://github.com/pandas-dev/pandas/blob/master/doc/cheatsheet/Pandas_Cheat_Sheet.pdf?
# dataSet = pd.concat([df1, df2])
# https://stackoverflow.com/questions/33763963/pandas-data-frame-headers-are-shifted-over-when-perfoming-csv-read?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
dataSet = pd.read_csv('data/iris.csv', index_col=False )


print(dataSet)
print(np.mean(dataSet, axis=0))
