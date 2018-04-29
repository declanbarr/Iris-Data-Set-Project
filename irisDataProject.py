# Declan Barr 31 Mar 2018
# Iris Flower Data Set Project for Programming and Scripting
# Using pandas to read csv files https://www.kaggle.com/ashokdavas/iris-data-analysis-pandas-numpy
# https://github.com/pandas-dev/pandas/blob/master/doc/cheatsheet/Pandas_Cheat_Sheet.pdf
# Setting headers for datafile: https://towardsdatascience.com/pca-using-python-scikit-learn-e653f8989e60
# Pairplot https://www.kaggle.com/mathewnik90/machinelearning-helloworld-with-iris-full-analysis
# Showing pairplots https://stackoverflow.com/questions/26597116/seaborn-plots-not-showing-up?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
# Boxplots https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.boxplot.html
# Histograms https://pandas.pydata.org/pandas-docs/stable/visualization.html

import pandas as pd # imports the pandas library as pd

pd.options.display.max_rows = 999 # Set max rows to 999 to ensure all rows are displayed (from https://pandas.pydata.org/pandas-docs/stable/options.html)
pd.options.display.max_columns = 100 # Set max columns to 100 to ensure all data is shown for describe() function (from https://pandas.pydata.org/pandas-docs/stable/options.html)

df = pd.read_csv('data/iris.csv', names=["Sepal Length", "Sepal Width", "Petal Length", "Petal Width", "Class"] ) # Read csv file and assigns the attribute names as headers to columns

print("Number of rows and columns: ", df.shape) # Provides the dimensions of the data set

print("The first 5 rows of the Iris Data Set are as follows: ")
print(df.head(5)) # Prints first 5 rows

print("The last 5 rows of the Iris Data Set are as follows: ")
print(df.tail(5)) # prints last 5 rows

print("The data contained in the Iris Data Set are as follows: ")
print(df) # Prints the Iris Data Set


print("Summary statistics for entire dataset: ") 
print(df.describe()) # Prints summary statistics (includes the count, mean, standard deviation, min, Q1, Q2, Q3 and Q4)

print("Summary statistics for each class of flower: ")
print(df.groupby(by='Class').describe()) # Prints summary statistics by class/ species


print("The variance for each attribute of the entire data set is: ")
print(df.var()) # Prints the variance for the entire data set

print("The variance for each attribute of each class of flower is: ")
print(df.groupby(by='Class').var()) # Prints the variance for each class


setosa = (df.iloc[0:50]) # Assigns the subset from rows 0 to 49 to setosa

versicolor = (df.iloc[50:100]) # Assigns the subset from rows 50 to 99 to versicolor

virginica = (df.iloc[100:150]) # Assigns the subset from rows 100 to 149 to virginica


import matplotlib.pyplot as plt # Imports the matplotlib.pyplot library as plt

# Boxplots
df.boxplot() # Produces boxplot for entire data set (produces outlier data points for Sepal Width)
plt.show() # Shows the boxplot created for entire data set

df.boxplot(column='Sepal Length',by='Class') # Produces boxplot for Sepal Length
plt.show() # Shows the boxplot created for Sepal Length
df.boxplot(column='Sepal Width',by='Class') # Produces boxplot for Sepal Width
plt.show() # Shows the boxplot created Sepal Width
df.boxplot(column='Petal Length',by='Class') # Produces boxplot for Petal Length
plt.show() # Shows the boxplot created for Petal Length
df.boxplot(column='Petal Width',by='Class') # Produces boxplot for Petal Width
plt.show() # Shows the boxplot created for Petal Width

# Histogram
df.plot.hist(title='Histogram for entire data set', bins=20, alpha=0.5) # Creates a histogram for the entire dataset
plt.show() # Shows the histogram created for the entire dataset
setosa.plot.hist(title='Histogram for Iris Setosa') # Creates a histogram for Iris Setosa
plt.show() # Shows the histogram created for Iris setosa
versicolor.plot.hist(title='Histogram for Iris Versicolor') # Creates a histogram for Iris Versicolor
plt.show() # Shows the histogram created for Iris versicolor
virginica.plot.hist(title='Histogram for Iris Virginica') # Creates a histogram for Iris Virginica
plt.show() # Shows the histogram created for Iris virginica


# Pairplot
import seaborn as sns # Imports the seaborn library as sns
sns.pairplot(df, hue='Class') # Creates a pairplot of the dataset with the different species coloured differently

plt.show() # Shows the pairplot created