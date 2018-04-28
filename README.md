# Iris Flower Data Set Project


## Project for Programming and Scripting Module


### Summary on the Iris Flower Data Set
#### Introduction
<p align="center">
  <img src="https://github.com/declanbarr/Iris-Data-Set-Project/blob/master/Ronald%20Fischer.jpg">
  <br><b>Ronald Fisher</b><br>
  
The Iris Flower Data Set was originally collected by Edgar Anderson in 1936. It consists of 50 samples for each of Iris setosa, Iris virginica and Iris versicolor; three related species of Iris flower. It is a multivariate data set meaning there is more than one variable. There are a total of 150 records under 5 attributes: petal length, petal width, sepal length, sepal width and class. [1]

<p align="center">
  <img src="https://github.com/declanbarr/Iris-Data-Set-Project/blob/master/Iris%20setosa.jpg">
  <img src="https://github.com/declanbarr/Iris-Data-Set-Project/blob/master/Iris%20virginica.jpg">
  <img src="https://github.com/declanbarr/Iris-Data-Set-Project/blob/master/Iris%20versicolor.jpg">
  <br><b>Iris setosa, Iris virginica and Iris versicolor</b><br>
<p align="center">
  <img src="https://github.com/declanbarr/Iris-Data-Set-Project/blob/master/Petal%20and%20Sepal%20length%20and%20width.jpg">
  <br><b>Measure of petal and sepal</b><br>

Ronald Fischer performed a Linear Discriminant on the data set which he detailed in his 1936 paper "The use of multiple measurements in taxonomic problems"[2]. The Linear Disciminant works on only 2 classes. The method was later developed into the Linear Discriminant analysis by C. R. Rao in 1948 "The utilization of multiple measurements in problems of biological classification"[3,4] This enables the analysis of more than two classes.

The Iris data set is used within the machine learning community to test out algorithms and visualisations. https://towardsdatascience.com/the-journey-of-a-machine-learning-model-from-building-to-retraining-fe3a37c32307. 


#### Linear discriminant analysis

The data set contains two clusters. One cluster contains Iris setosa and the other contains Iris virginica and Iris versicolor.[1]
![alt text](https://github.com/declanbarr/Iris-Data-Set-Project/blob/master/Ldaseparation.png)[5]

(needs to be rewritten)
Linear discriminant analysis is a method for maximising the separability of known categories. In LDA information from two variables are combined into a single axis in a way that maximizes the separation of the two categories, see pic above. The new axis is created according to two critera which are considered simultaneously:
1. Maximize the distance between means (mu)
2. Minimize the variation (s^2) within each category

This can be achieved by the following formula:

(mu1 - mu2)^2/(s1^2 + s2^2) 

The numerator is esentially the square of the distance between the two means and can therefore be rewritten as d^2:

d^2/(s1^2 + s2^2) 

Ideally d^2 should be very large and (s1^2 + s2^2) should be very small. When there are 3 categories, the means for each category is measured from a central point. This central point is central to all points in the dataset. There will also need to be 2 axis to separate the data rather that 1 which is needed if there is only 2 categories.[6]

Linear discriminant analysis can only be used on the iris data set when the species are known. When the species are not known the Nonlinear Dimensionality Reduction technique of Nonlinear Principal Component Analysis is able to separte the data based on species.[1]

#### Principal component analysis

#### Non linear principal component analysis

#### Support Vector Machines

#### cluster analysis

#### data mining

#### nonlinear branching principal component

#### metro map



### Investigating a data set

A range of tools can be used to help identify patterns in a data set such as visualisation and statistical analysis. (http://ngss.nsta.org/Practices.aspx?id=4) 

Some examples of data visualisations are histograms, boxplots and scatterplots. 

Histograms are used to represent the distribution of numerical data. (https://en.wikipedia.org/wiki/Histogram). They enable a data set to be investigated for outliers and for skewness. https://statistics.laerd.com/statistical-guides/understanding-histograms.php.

Box plots are also used to represent distribution. Box plots represent the five number summary: minimum, first quartile, second quartile or median, third quartile and maximum. http://www.physics.csbsju.edu/stats/box2.html

Scatter plots use dots to represent individual data points. They are useful to see if there is a relationship between two variables. http://www.statisticshowto.com/probability-and-statistics/regression-analysis/scatter-plot-chart/

(Add pictures of histograms, boxplots and scatterplots)

Some basic statistical analysis can involve calculating the average and calculating the spread of the data. Mean and median are two ways of calculating the average of a data set. Mean involves summing all values and then dividing by the number of values. Median is the middle data point. The mean can be skewed by outliers https://www.skillsyouneed.com/num/simple-statistical-analysis.html
Spread can be measured by the standard deviation, variance or range. The range is the simplest measure of spread and is simply the maximum minus the minimum value. Variance is the sum of the squares of the distance of each value from the mean divided by the number of values. The standard deviation is the square root of the variance. https://www.sciencebuddies.org/science-fair-projects/science-fair/variance-and-standard-deviation. 




Python can be used to investigate a data set by enabling the data to be visualised as well as carrying out the statisical analysis. This can be done by the use of libraries which need to be imported, such as pandas, matplotlib and seaborn. Firstly the data set needs to be read. This can be achieved using the pandas library with the following code:

Input:
```Python
import pandas
df = pd.read_csv('data/iris.csv', names=["Sepal Length", "Sepal Width", "Petal Length", "Petal Width", "Class"]
```
This creates a pandas dataframe called "df" which contains the data from the csv file iris.csv. A data frame is two-dimensional data structure where the data is arranged in rows and columns. (https://www.tutorialspoint.com/python_pandas/python_pandas_dataframe.htm). In this case the columns are assigned the names "Sepal Length", "Sepal Width", "Petal Length", "Petal Width" and "Class". 

The statisical summary of the data set can be given by typing the following:

Input:
```Python
df.describe()
```
This will give the count (number of rows), mean, standard deviation, min, 25 % (or Q1), 50 % (or Q2/median), 75% (or Q3) and maximum.

The following code will allow the data to be visualised by providing a histogram:

Input:
```Python
df.plot.hist()
```

### Summary of Investigations

For this project I used Anaconda version 5.0.1 and Python version 3.6.3. Anaconda is a free and open source distribution of Python used for data science (https://en.wikipedia.org/wiki/Anaconda_(Python_distribution). Anaconda provides a number of libraries. For this project I will be using the following libraries: Pandas, Seaborn and Matplotlib.

This Iris Flower Data Set can be downloaded from [UCI's Machine Learning Repository](https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data). It is also included in this repository in the folder [data](https://github.com/declanbarr/Iris-Data-Set-Project/tree/master/data) as [iris.csv](https://github.com/declanbarr/Iris-Data-Set-Project/blob/master/data/iris.csv).The python script that I wrote to investigate the data set is also contained within this repository and is named [irisDataProject.py](https://github.com/declanbarr/Iris-Data-Set-Project/blob/master/irisDataProject.py).

To run this script simply download it to a folder and in the same folder have folder named data with this iris data set inside. It must be named iris.csv in order to be read correctly. In the terminal change working directory to the folder containing the python script and data folder. Then type "python irisDataProject.py". The following will then show within the terminal:   
   * Dimensions of data set
    * First 5 rows
    * Last 5 rows
    * All 150 rows
    * Summary statistics for entire data set
        * Count
        * Mean
        * STD (Standar Deviation)
        * Min
        * 25 %
        * 50 %
        * 75 %
        * Max
    * Summary statistics for each class of flower
    * The variance for each attribute of the entire data set
    * The Variance for each attribute for each class of Iris flower

Then a number of graphs will show:
    * Boxplots for
        * entire data set
        * each attribute
    * Histogram for
        * entire data set
        * each class
    * Pairplots
        * each attribute



All values in this write up will be given to 1 decimal place.

The Iris flower data set has the following dimensions:
```
(150, 5)
```
The first and last 5 rows of the data set are:
```
   Sepal Length  Sepal Width  Petal Length  Petal Width        Class
0           5.1          3.5           1.4          0.2  Iris-setosa
1           4.9          3.0           1.4          0.2  Iris-setosa
2           4.7          3.2           1.3          0.2  Iris-setosa
3           4.6          3.1           1.5          0.2  Iris-setosa
4           5.0          3.6           1.4          0.2  Iris-setosa
```
and
```
     Sepal Length  Sepal Width  Petal Length  Petal Width           Class
145           6.7          3.0           5.2          2.3  Iris-virginica
146           6.3          2.5           5.0          1.9  Iris-virginica
147           6.5          3.0           5.2          2.0  Iris-virginica
148           6.2          3.4           5.4          2.3  Iris-virginica
149           5.9          3.0           5.1          1.8  Iris-virginica

```

We can see that the first column contains the index number, followed by 4 columns containing the Sepal length, Sepal width, Petal length and Petal width, respectively. The last column contains the species or class of Iris flower. The first and last row is contained in index 0 and 149 respectively. 

The summary statisitics for the entire data set are:
```
       Sepal Length  Sepal Width  Petal Length  Petal Width
count    150.000000   150.000000    150.000000   150.000000
mean       5.843333     3.054000      3.758667     1.198667
std        0.828066     0.433594      1.764420     0.763161
min        4.300000     2.000000      1.000000     0.100000
25%        5.100000     2.800000      1.600000     0.300000
50%        5.800000     3.000000      4.350000     1.300000
75%        6.400000     3.300000      5.100000     1.800000
max        7.900000     4.400000      6.900000     2.500000
```
Petal width has the lowest value at 0.1 cm and sepal length has the highest value at 7.9 cm.

The sepal length has the highest mean at 5.8 cm and the petal length has the lowest at 1.2 cm. The median value can also be seen here as it is the 50% value. This is also highest for sepal length at 5.8 cm and lowest for petal width at 1.3 cm. For sepal length and sepal width the mean and median values are quite similar with values of 5.8 cm and 5.8 cm for sepal length and 3.1 cm (3.05 cm correct to 2 d.p.) and 3.0 cm for sepal width, respectively. However, the mean and median values for petal length and petal width differ from each other with values of 3.8 cm and 4.4 cm for petal length and 1.2 cm and 1.3 cm for petal width. This suggests that the data for petal length and width is skewed towards the lower values.

The petal length has the highest standard deviation at 1.8 cm and sepal width has the lowest at 0.4 cm. 

<p align="center">
  <img src="https://github.com/declanbarr/Iris-Data-Set-Project/blob/master/boxPlotIrisDataSet.png">
  <br><b>Boxplot for Iris flower data set</b><br>
  
From the boxplot above the large and small spreads can be seen for petal length and sepal width, respectively,. The range of values (the distance between maximum and minimum values) as well as the interquartile range (the distance between the 75% and 25% values) are largest for petal length and smallest for sepal width, just as the standard deviation was found to be from the statistical summary above. The petal length therefore has the highest spread of data and sepal width has the lowest.

<p align="center">
  <img src="https://github.com/declanbarr/Iris-Data-Set-Project/blob/master/histogramIrisDataSet.png">
  <br><b>Histogram for Iris flower data set</b><br>
  
From the histogram above we can also see the spread of data with petal length again having the highest value. However, we can also see that the data is quite unevenly distributed. There a two clusters of data in the histogram for petal length. One from ~1 cm to ~2 cm and the other from ~3 cm to ~7 cm. This information could not be seen from the boxplots above. Petal width also appears to have an uneven distribution, with a cluster from around 0 to 0.5 cm and another from ~1 cm to ~3 cm. These clusters may represent differnt classes of flowers.


Summary statistics for each class of flower:
```
                Petal Length                                               \
                       count   mean       std  min  25%   50%    75%  max
Class
Iris-setosa             50.0  1.464  0.173511  1.0  1.4  1.50  1.575  1.9
Iris-versicolor         50.0  4.260  0.469911  3.0  4.0  4.35  4.600  5.1
Iris-virginica          50.0  5.552  0.551895  4.5  5.1  5.55  5.875  6.9

                Petal Width                                            \
                      count   mean       std  min  25%  50%  75%  max
Class
Iris-setosa            50.0  0.244  0.107210  0.1  0.2  0.2  0.3  0.6
Iris-versicolor        50.0  1.326  0.197753  1.0  1.2  1.3  1.5  1.8
Iris-virginica         50.0  2.026  0.274650  1.4  1.8  2.0  2.3  2.5

                Sepal Length                                              \
                       count   mean       std  min    25%  50%  75%  max
Class
Iris-setosa             50.0  5.006  0.352490  4.3  4.800  5.0  5.2  5.8
Iris-versicolor         50.0  5.936  0.516171  4.9  5.600  5.9  6.3  7.0
Iris-virginica          50.0  6.588  0.635880  4.9  6.225  6.5  6.9  7.9

                Sepal Width
                      count   mean       std  min    25%  50%    75%  max
Class
Iris-setosa            50.0  3.418  0.381024  2.3  3.125  3.4  3.675  4.4
Iris-versicolor        50.0  2.770  0.313798  2.0  2.525  2.8  3.000  3.4
Iris-virginica         50.0  2.974  0.322497  2.2  2.800  3.0  3.175  3.8
```



<p align="center">
  <img src="https://github.com/declanbarr/Iris-Data-Set-Project/blob/master/boxplotSepalLength.png">
  <img src="https://github.com/declanbarr/Iris-Data-Set-Project/blob/master/boxplotSepalWidth.png">
  <img src="https://github.com/declanbarr/Iris-Data-Set-Project/blob/master/boxPlotPetalLength.png">
  <img src="https://github.com/declanbarr/Iris-Data-Set-Project/blob/master/boxPlotPetalWidth.png">
  <br><b>Boxplots for the different attributes in the Iris flower data set</b><br>

The boxplots above show that the clusters for petal length and width that could be seen in the histogram above represent the Iris setosa and both of Iris virginica and Iris versicolor. It is therefore possible to distinguish Iris setosa from the other two classes of flower using only one attribute; either petal length or width. It is not possible to distinguish Iris versicolor from Iris virginica using only one attribute.

<p align="center">
  <img src="https://github.com/declanbarr/Iris-Data-Set-Project/blob/master/irisDataSetPairplot.png">
  <br><b>Pairplot for the different attributes in the Iris flower data set</b><br>

In the above pairplot we can see scatter plots for one attribute against another. Where an attribute is plotted against itself a histogram is produced. We can see in the histograms for petal length and petal width that Iris setosa is easily separable from the other two species just like the boxplots above. In the scatter plots, in almost all cases the Iris setosa is easily separable from the other two classes (except when sepal width is plotted against sepal length).


(Add analyses done by others on this)


http://scikit-learn.org/stable/auto_examples/decomposition/plot_pca_vs_lda.html



(Switched to using seaborn to display boxplots as pandas was combining multiple boxplots into one)

#### References
[1] Wikipedia. Iris flower data set
[https://en.wikipedia.org/wiki/Iris_flower_data_set]

[2] Annals of Eugenics. The use of multiple measurements in taxonomic problems.
[https://onlinelibrary.wiley.com/doi/epdf/10.1111/j.1469-1809.1936.tb02137.x]

[3] Wikipedia. Linear discriminant analysis
https://en.wikipedia.org/wiki/Linear_discriminant_analysis

[4] Journal of the Royal Statistical Society. The utilization of multiple measurements in problems of biological classification
https://www.jstor.org/stable/2983775?seq=1#page_scan_tab_contents

[5] Free code camp. The Curse of Dimensionality
https://medium.freecodecamp.org/the-curse-of-dimensionality-how-we-can-save-big-data-from-itself-d9fa0f872335

[6] StatQuest. Linear Discriminant Analysis (LDA), clearly explained
https://statquest.org/2016/07/10/statquest-linear-discriminant-analysis-lda-clearly-explained/

### Project Plan
#### Research background information about the data set and write a summary about it.
##### Completion date: ~3rd April 2018~ ~12th April 2018~ ~19th April 2018~ (using contingency week here)(To be completed in parallel with "Summarise the Data Set")
##### To be tidied up before completion data of 29th April 2018 - No major new topics to be introduced
* Read wikipedia article on Iris Flower Data Set
    * ~Introduction~
    * Use of the data set
        * ~First two paragraphs~
        * Last paragraph (too many unkown terms)
* Read unknown terms from Iris Flower Data Set on wikipedia  
    * ~linear discriminant analysis/model~ https://www.youtube.com/watch?v=azXCzI57Yfc
    * support vector machines
    * cluster analysis (also explain what a cluster is)
    * data mining
    * nonlinear branching principal component
    * metro map
    * Nonlinear Principal Component Analysis
* Read references on Iris Flower Data Set on wikipedia
    * ~Edgar Anderson (1936). "The species problem in Iris"~ (contains a lot of irrelevant information for this project)
    * R. A. Fisher (1936). "The use of multiple measurements in taxonomic problems"
    * A. N. Gorban, A. Zinovyev. Principal manifolds and graphs in practice: from molecular biology to dynamical systems
    * UCI Machine Learning Repository: Iris Data Set
        * Duda,R.O., & Hart,P.E. (1973) Pattern Classification and Scene Analysis. (Q327.D83) John Wiley & Sons. ISBN 0-471-22361-1. See page 218. 
        * Dasarathy, B.V. (1980) "Nosing Around the Neighborhood: A New System Structure and Classification Rule for Recognition in Partially Exposed Environments". IEEE Transactions on Pattern Analysis and Machine Intelligence, Vol. PAMI-2, No. 1, 67-71. 
        * Gates, G.W. (1972) "The Reduced Nearest Neighbor Rule". IEEE Transactions on Information Theory, May 1972, 431-433. 
    * On Using Class-Labels in Evaluation of Clusterings
    * Topological grammars for data approximation
    * Will the real iris data please stand up?
    
* Type up summary (This would be best to be done immediatley instead of typing everything up at the end)
    * Find out how to do symbol such as mu
#### Summarise the data set
##### Completion date: ~12th April 2018~ 19th April 2018 (using contingency week here)
##### Summarise each investigation as it has been completed

* For each species calculate:
   * ~Five-number summary (see https://en.wikipedia.org/wiki/Five-number_summary)~
      * ~min~
      * ~Q1~
      * ~Q2 (technically median)~
      * ~Q3~
      * ~Max~
   * Average
      * ~Mean~
      * ~Mode~ (not needed for this project)  
      * ~Median~
   * Spread
      * ~Variance~
      * ~Standard Deviation~
      * ~IQR (Boxplot to be used to display IQR)~
      * ~Range (Boxplot to be used to display range)~
* ~Boxplots - produce boxplots comparing the same attribute across different species~
* ~Read https://warwick.ac.uk/fac/sci/moac/people/students/peter_cock/r/iris_plots/~
    * S~catter plots of sw, sl, pl and pw. See https://www.kaggle.com/mathewnik90/machinelearning-helloworld-with-iris-full-analysis for pair plots~
    * Can relationships be made between sizes eg
        * sl/sw and plot against pl/pw?
        * sw times sl plotted against pw times pl?
        * 1/sw plotted against 1/sl
        * plot of area of sepal vs area of peta
        * 1/ log sw etc
        * multiply or divide a feature by a factor
        * etc
        * Is this what machine learning does? 
* ~Produce graphs, see http://www.statisticshowto.com/types-graphs/#segmentedbartypes~


* Reference other peoples interesing analyses of the data set
    * Perform LDA on data set - show before and after pictures to illustrate how LDA has improved the separation of the data points (these pictures are to be added to summarise investigations below
    * PCA
    * Neural networks
    * 
 
* Glossary of terms - provide a link from each term to a definition either at the bottom of the readme or to a separte file in the project folder/ provide link to wikipedia
#### Summarise investigations 
##### Completion date: ~21st April 2018~ 28th April 2018 (moved back due to use of contingency week)






#### ~Contingency week~
##### Completion date: 29th April 2018

