# Declan Barr 31 Mar 2018
# Iris Flower Data Set Project for Programming and Scripting
# Using pandas to read csv files https://www.kaggle.com/ashokdavas/iris-data-analysis-pandas-numpy
# https://github.com/pandas-dev/pandas/blob/master/doc/cheatsheet/Pandas_Cheat_Sheet.pdf
# Setting headers for datafile: https://towardsdatascience.com/pca-using-python-scikit-learn-e653f8989e60
# Pairplot https://www.kaggle.com/mathewnik90/machinelearning-helloworld-with-iris-full-analysis
# Showing pairplots https://stackoverflow.com/questions/26597116/seaborn-plots-not-showing-up?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa

import pandas as pd

df = pd.read_csv('data/iris.csv', names=["Sepal Length", "Sepal Width", "Petal Length", "Petal Width", "Class"] ) # Read csv file and assigns headers to columns

print(df.head(5)) # Prints first 5 rows
print(df.tail(5)) # prints last 5 rows
print("Number of rows and columns: ", df.shape) 

setosaSepalLength = df.iloc[0:50,[0]] # Assigns the subset from rows 0 to 49 of column 0 to setosaSepalLength
print("Minimum value: ", setosaSepalLength.min()) # Prints the minimum value of the setosaSepalLength subset
print("Maximum value: ", setosaSepalLength.max()) # Prints the maximum value of the setosaSepalLength subset
print("Mean value: ", setosaSepalLength.mean()) # Prints the mean value of the setosaSepalLenght subset

print("Summary statistics for entire dataset: ") 
print(df.describe()) # Prints summary statistics (includes the count, mean, standard deviation, min, Q1, Q2, Q3 and Q4)

setosa = (df.iloc[0:50]) # Assigns the subset from rows 0 to 49 to setosa
print("Summary statistics for Iris setosa: ")
print(setosa.describe()) # Prints summary statistics for the setosa subset

versicolor = (df.iloc[50:100]) # Assigns the subset from rows 50 to 99 to versicolor
print("Summary statistics for Iris versicolor: ")
print(versicolor.describe()) # Prints summary statistics for the versicolor subset

virginica = (df.iloc[100:150]) # Assigns the subset from rows 100 to 149 to virginica
print("Summary statistics for Iris virginica: ")
print(virginica.describe()) # Prints summary statistics for the virginica subset


import matplotlib.pyplot as plt

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
df.plot.hist(title='Histogram for entire data set') # Creates a histogram for the entire dataset
plt.show()
setosa.plot.hist(title='Histogram for Iris Setosa') # Creates a histogram for Iris Setosa
plt.show()
versicolor.plot.hist(title='Histogram for Iris Versicolor') # Creates a histogram for Iris Versicolor
plt.show()
virginica.plot.hist(title='Histogram for Iris Virginica') # Creates a histogram for Iris Virginica
plt.show()

# Pairplot

import seaborn as sns
g = sns.pairplot(df, hue='Class') # Creates a pairplot of the dataset with the different species coloured differently

plt.show() # Shows the pairplot created