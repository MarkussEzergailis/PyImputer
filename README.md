### Context and Task

Most data science projects start by pre-processing a dataset to ensure the data is ready to use for its intended purpose. One of the tasks that a datascientist would typically complete during such a pre-processing phase is to replace missing data values in the dataset using a process known as imputation. A popular toolkit that assist with this task in python is class sklearn.preprocessing.Imputer. 
A discussion of this class and its properties and methods can be found at http://lijiancheng0614.github.io/scikit-learn/modules/generated/sklearn.preprocessing.Imputer.html . 

You are required to design and implement your own version of class Imputer. Your version should make use of the **strategy pattern** to ensure it is extensible and easy to maintain. 

### Specifications
#### Initial Parameters
Your class Imputer should (initially) accept  should accept two parameters, namely strategy and axis with the following options: 

**strategy** : string, optional (default=”mean”).
The imputation strategy.
-	If “mean”, then replace missing values using the mean along the axis. 
-	If “median”, then replace missing values using the median along the axis.
-	If “mode”, then replace missing using the most frequent value along the axis.
Important: It should be possible to add an additional strategy without affecting any of the existing strategy implementations.

**axis** : integer, optional (default=0) 
The axis along which to impute.
-	If axis=0, then impute along columns.
-	If axis=1, then impute along rows. (Not to be implemented now)
Note: Initially **we will only impute along columns as the axis you DO NOT need to write any code for dealing with the axis = 1**. 


#### Methods
Your class should support two methods, namely fit and transform with the following behaviours:

#### fit : *fit(X)*
- fit the imputer on X.

Parameters:	
- X : {array-like, sparse matrix}, shape (n_samples, n_features)
- Input data, where n_samples is the number of samples and n_features is the number of features.

Returns:	
- self : object
- Returns self.

In other words: Fit receives as input the "matrix" of incomplete data, with the "boundaries" of the area for which we want to impute (calculate) missing values. (i.e. a single column, or the entire matrix) and returns an object containing only the part we want to do the imputation on. 


#### transform : *transform(X)*
- Impute all missing values in X and returns X with new values.

Parameters:	
- X : {array-like, sparse matrix}, shape = [n_samples, n_features]
- The input data to complete.
