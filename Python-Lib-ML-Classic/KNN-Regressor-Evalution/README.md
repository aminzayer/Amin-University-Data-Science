# KNN-Regressor-Evalution
Implementation of KNN in Python KNN-Regressor &amp; KNN Predict &amp; Evalution
# KNN-Regressor-Practice

## Implementation of KNN in Python KNN-Regressor & KNN Predict & Evalution
## [[3, 4, 5], [6, 9, 7], [2, 4, 5],[1, 3, 2], [7, 7, 7], [5, 6,7], [4, 4 ,8],[2, 2, 2],[3 ,5 ,1]]

## With This Label for Classification=> [1,2,1,1,2,2,2,1,1]
## Test Data ==> [5 ,5 ,5] , [6 , 3 ,2]
"""
```python
import pandas as pd
import numpy as np
```
# Load the Dataset
## Create DataFrame from Train Data

# Use Pandas lib for Create Dataframe
```python
TrainData = pd.DataFrame([[3, 4, 5, 1],
                         [6, 9, 7, 2],
                         [2, 4, 5, 1],
                         [1, 3, 2, 1],
                         [7, 7, 7, 2],
                         [5, 6, 7, 2],
                         [4, 4 ,8, 2],
                         [2, 2, 3, 1],
                         [3, 5, 1, 1]],columns=['F1', 'F2', 'F3','Label'])
print('Show Train Data')
TrainData
```
## Create DataFrame from Test Data
```python
TestData = pd.DataFrame([[5, 5, 5, 0],
                         [6, 3, 2, 0]],columns=['F1', 'F2', 'F3','Label'])
print('Show Test Data')
TestData
```
## Select the Features

# Train Data
```python
X_train = TrainData.iloc[:,[0,1,2]].values # Features Data
Y_train = TrainData.iloc[:,[3]].values     # Labeled Data

# Test Data
X_test = TestData.iloc[:,[0,1,2]].values
Y_test = TestData.iloc[:,[3]].values

# Show Train Data
X_train,Y_train

# Show Test Data
X_test,Y_test
```
### Define Error Metrics
#### As this is a regression problem, we have defined MAPE as the error metrics as shown below

```python
def MAPE(Y_actual,Y_Predicted):
    Mape = np.mean(np.abs((Y_actual - Y_Predicted)/Y_actual))*100
    return Mape
```
## Build the Model of KNN Classification

#Building the KNN.Regressor Model on our dataset
```python
k=3
from sklearn.neighbors import KNeighborsClassifier
KNN_model = KNeighborsClassifier(n_neighbors=k,metric='euclidean') # euclidean & minkowski & manhattan & 
KNN_model.fit(X_train,Y_train.ravel())
```
**The following lists the string metric identifiers and the associated distance metric classes:**

**Metrics intended for real-valued vector spaces:**

#### “euclidean”  = > sqrt(sum((x - y)^2))

#### “manhattan” => sum(|x - y|)

#### “chebyshev” => max(|x - y|)

#### “minkowski” => sum(|x - y|^p)^(1/p)

#### “wminkowski” => sum(|w * (x - y)|^p)^(1/p)

#### “seuclidean” => sqrt(sum((x - y)^2 / V))

#### “mahalanobis” => sqrt((x - y)' V^-1 (x - y))

### Predict the testing Data

```python
KNN_predict = KNN_model.predict(X_test)  # Predictions on Testing data

X_test

Y_test = KNN_predict # Set Predicted label put on Y_Test
Y_test   # Predicted Values
```
## Accuracy Check For KNN Classification !

# Using MAPE error metrics to check for the error rate and accuracy level
```python
KNN_MAPE = MAPE(Y_train,KNN_predict)
Accuracy_KNN = 100 - KNN_MAPE
print("MAPE: ",KNN_MAPE)
print('Accuracy of KNN model: {:0.2f}%.'.format(Accuracy_KNN))
```
## Build the Model of KNN Regressor Classification

#Building the KNN.Regressor Model on our dataset
```python
k=3
from sklearn.neighbors import KNeighborsRegressor
KNN_model = KNeighborsRegressor(n_neighbors=k).fit(X_train,Y_train)
```
### Predict the testing Data
```python
KNN_predict = KNN_model.predict(X_test) #Predictions on Testing data

X_test

Y_test = KNN_predict # Set Predicted label put on Y_Test
Y_test   # Predicted Values
```
## Accuracy Check For KNN Regressor Classification!

# Using MAPE error metrics to check for the error rate and accuracy level
```python
KNN_MAPE = MAPE(Y_train.reshape(1, -1),KNN_predict)
Accuracy_KNN = 100 - KNN_MAPE
print("MAPE: ",KNN_MAPE)
print('Accuracy of KNN model: {:0.2f}%.'.format(Accuracy_KNN))
```

## Authors

Amin Zayeromali

![Profile views](https://visitor-badge.glitch.me/badge?page_id=aminzayer.aminzayer)

[![Github](https://img.shields.io/github/followers/aminzayer?label=Follow&style=social)](https://github.com/aminzayer)

Twitter: [@AminZayeromali](https://twitter.com/aminzayeromali)

Instagram: [aminzayer](https://www.instagram.com/aminzayer/)

Linkedin: [aminzayeromali](https://ir.linkedin.com/in/aminzayeromali)

Google Scolar: [Amin Zayeromali](https://scholar.google.com/citations?user=IDR8QvcAAAAJ&hl=en)

Email : [Amin {dot} zayeromali {At} gmail {dot} com](&#109;&#097;&#105;&#108;&#116;&#111;:&#097;&#109;&#105;&#110;&#046;&#122;&#097;&#121;&#101;&#114;&#111;&#109;&#097;&#108;&#105;&#064;&#103;&#109;&#097;&#105;&#108;&#046;&#099;&#111;&#109;)


<h2> Connect with me </h2>
<a href = 'https://www.linkedin.com/in/aminzayeromali'> <img width = '32px' align= 'center' src="https://raw.githubusercontent.com/rahulbanerjee26/githubAboutMeGenerator/main/icons/linked-in-alt.svg"/></a> 
<a href = 'https://twitter.com/AminZayeromali'> <img width = '32px' align= 'center' src="https://raw.githubusercontent.com/rahulbanerjee26/githubAboutMeGenerator/main/icons/twitter.svg"/></a> 
<a href = 'https://aminzayer.ir/'> <img width = '32px' align= 'center' src="https://raw.githubusercontent.com/rahulbanerjee26/githubAboutMeGenerator/main/icons/portfolio.png"/></a> 
<a href = 'https://www.github.com/aminzayer'> <img width = '32px' align= 'center' src="https://raw.githubusercontent.com/rahulbanerjee26/githubAboutMeGenerator/main/icons/github.svg"/></a>
<br>


## License

This project is licensed under the MIT License - see the LICENSE.md file for details
