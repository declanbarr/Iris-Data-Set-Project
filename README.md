# Iris Flower Data Set Project


## Project for Programming and Scripting Module


### Summary on the Iris Flower Data Set

[https://en.wikipedia.org/wiki/Iris_flower_data_set]
#### Wiki intro
The Iris Flower Data Set is a data set collected by Edgar Anderson. It consists of 50 samples for each of Iris setosa, Iris virginica and Iris versicolor; three related species of Iris flower. It is a multivariate data set meaning there is more than one variable. There are a total of 150 records under 5 attributes: petal length, petal width, sepal length, sepal width and class. (picture on petals and sepals)

Ronald Fischer used the data set to perform a linear discriminant analysis which he detailed in his 1936 paper The use of multiple measurements in taxonomic problems. A linear discriminant analysis is .....

#### Use of the data set
Data set contains two clusters. One cluster contains Iris setosa and the other contains Iris virginica and Iris versicolor. (provdie pictures on flowers) 

(Provide link to wikipedia article above and to Fischer's 1936 paper)

[https://archive.ics.uci.edu/ml/datasets/iris]
* Includes download of dataset (provide instructions?)
* Explanation of the data set
* References to read (see project plan)

#### Linear discriminant analysis
https://www.youtube.com/watch?v=azXCzI57Yfc

(make reference to above about how clusters of Iris virginica and Iris versicolor aren't easily separable)
Linear discriminant analysis is a method for maximising the separability of known categories. In LDA information fromm two variables are combined into a single axis in a way that maximizes the separation of the two categories. See pic below

![alt text](https://github.com/declanbarr/Iris-Data-Set-Project/blob/master/LDA.png)
source: https://qph.ec.quoracdn.net/main-qimg-de0e3fbb98f88884fcc75f6488360602

The new axis is created according to two critera which are considered simultaneously:
1. Maximize the distance between means (mu)
2. Minimize the variation s^2 within each category

(mu1 - mu2)^2/(s1^2 + s2^2) 

The numerator is esentially the square of the distance between the two means and can therefore be rewritten as d^2:

d^2/(s1^2 + s2^2) 

Ideally d^2 should be very large and (s1^2 + s2^2) should be very small.

When there are 3 categories, the means for each category is measured from a central point. This central point is central to all points in the dataset. There will also need to be 2 axis to separate the data rather that 1 which is needed if there is only 2 categories.




   
### Project Plan
#### Research background information about the data set and write a summary about it.
##### Completion date: ~3rd April 2018~ 12th April 2018 (To be completed in parallel with "Summarise the Data Set")
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
##### Completion date: 12th April 2018
* For each species calculate:
   * Five-number summary (see https://en.wikipedia.org/wiki/Five-number_summary)
      * min
      * Q1
      * Q2 (technically median)
      * Q3
      * Max
   * Average
      * Mean
      * Mode
      * Median
   * Spread
      * Variance
      * Standard Deviation
      * IQR
      * Range
* Read https://warwick.ac.uk/fac/sci/moac/people/students/peter_cock/r/iris_plots/
    * Scatter plots of sw, sl, pl and pw.
    * Can relationships be made between sizes eg
        * sl/sw and plot against pl/pw?
        * sw times sl plotted against pw times pl?
        * 1/sw plotted against 1/sl
        * plot of area of sepal vs area of peta
        * 1/ log sw etc
        * multiply or divide a feature by a factor
        * etc
        * Is this what machine learning does? 
* Produce graphs, see http://www.statisticshowto.com/types-graphs/#segmentedbartypes
* Perform LDA on data set - show before and after pictures to illustrate how LDA has improved the separation of the data points (these pictures are to be added to summarise investigations below
#### Summarise investigations
##### Completion date: 21st April 2018


#### Contingency week
##### Completion date: 29th April 2018

