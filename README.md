# Iris Flower Data Set Project


## Project for Programming and Scripting Module


### Summary on the Iris Flower Data Set
#### Introduction
<p align="center">
  <img src="https://github.com/declanbarr/Iris-Data-Set-Project/blob/master/Ronald%20Fischer.jpg">
  <br><b>Ronald Fisher</b><br>
  
The Iris Flower Data Set is a data set collected by Edgar Anderson. It consists of 50 samples for each of Iris setosa, Iris virginica and Iris versicolor; three related species of Iris flower. It is a multivariate data set meaning there is more than one variable. There are a total of 150 records under 5 attributes: petal length, petal width, sepal length, sepal width and class. [1]

<p align="center">
  <img src="https://github.com/declanbarr/Iris-Data-Set-Project/blob/master/Iris%20setosa.jpg">
  <img src="https://github.com/declanbarr/Iris-Data-Set-Project/blob/master/Iris%20virginica.jpg">
  <img src="https://github.com/declanbarr/Iris-Data-Set-Project/blob/master/Iris%20versicolor.jpg">
  <br><b>Iris setosa, Iris virginica and Iris versicolor</b><br>
<p align="center">
  <img src="https://github.com/declanbarr/Iris-Data-Set-Project/blob/master/Petal%20and%20Sepal%20length%20and%20width.jpg">
  <br><b>Measure of petal and sepal</b><br>

Ronald Fischer performed a Linear Discriminant on the data set which he detailed in his 1936 paper "The use of multiple measurements in taxonomic problems"[2]. The Linear Disciminant works on only 2 classes. The method was later developed into the Linear Discriminant analysis by C. R. Rao in 1948 "The utilization of multiple measurements in problems of biological classification"[3,4] This enables the analysis of more than two classes.


[https://archive.ics.uci.edu/ml/datasets/iris]
* Includes download of dataset (provide instructions?)
* Explanation of the data set
* References to read (see project plan)


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




### Summary of Investigations

(need to write in what version of python, anaconda etc)
(need to write what investigating a data set entails and how python can be used to do it)
    * what a library is
    * how to import etc

This Iris Flower Data Set can be downloaded from [UCI's Machine Learning Repository](https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data). The python script that I wrote to investigate the data set is contained within this repository and is named [irisDataProject.py](https://github.com/declanbarr/Iris-Data-Set-Project/blob/master/irisDataProject.py).

List libraries used

(What is a dataframe)
The following code can be used to create a dataframe from the Iris flower data set and assign headers to the colums:

(reference to pandas cheat sheet)

(Box plot producing outlier data points)

(Try to produce box plot for different flowers for the same attribute)




All values in this write up will be given to 1 decimal place


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

We can see that the first 4 columns contain the Sepal length, Sepal width, Petal length and Petal width. The last column contains the species or class of Iris flower.

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

<p align="center">
  <img src="https://github.com/declanbarr/Iris-Data-Set-Project/blob/master/boxplotSepalLength.png">
  <img src="https://github.com/declanbarr/Iris-Data-Set-Project/blob/master/boxplotSepalWidth.png">
  <img src="https://github.com/declanbarr/Iris-Data-Set-Project/blob/master/boxPlotPetalLength.png">
  <img src="https://github.com/declanbarr/Iris-Data-Set-Project/blob/master/boxPlotPetalWidth.png">
  <br><b>Boxplots for the different attributes in the Iris flower data set</b><br>

The boxplots above show that the clusters for petal length and width that could be seen in the histogram above represent the Iris setosa and both of Iris virginica and Iris versicolor. It is therefore possible to distinguish Iris setosa from the other two classes of flower using only one attribute; either petal length or width. It is not possible to distinguish Iris versicolor from Iris virginica using only one attribut.

<p align="center">
  <img src="https://github.com/declanbarr/Iris-Data-Set-Project/blob/master/irisDataSetPairplot.png">
  <br><b>Pairplot for the different attributes in the Iris flower data set</b><br>

In the above pairplot we can see scatter plots for one attribute against another. Where an attribute is plotted against itself a histogram is produced. In almost all cases the Iris setosa is easily separable from the other two classes (except when sepal width is plotted against sepal length).


(Add analyses done by others on this)



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

* How to download dataset
* How to run code




#### ~Contingency week~
##### Completion date: 29th April 2018

