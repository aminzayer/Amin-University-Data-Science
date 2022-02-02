# KNN-Regressor-Practice

## Implementation of KNN in Python KNN-Regressor & KNN Predict & Evalution
## [[3, 4, 5], [6, 9, 7], [2, 4, 5],[1, 3, 2], [7, 7, 7], [5, 6,7], [4, 4 ,8],[2, 2, 2],[3 ,5 ,1]]

## With This Label for Classification=> [1,2,1,1,2,2,2,1,1]
## Test Data ==> [5 ,5 ,5] , [6 , 3 ,2]


import pandas as pd
import numpy as np

# Load the Dataset
## Create DataFrame from Train Data


# Use Pandas lib for Create Dataframe
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
## Create DataFrame from Test Data

TestData = pd.DataFrame([[5, 5, 5, 0],
                         [6, 3, 2, 0]],columns=['F1', 'F2', 'F3','Label'])
print('Show Test Data')
TestData

## Select the Features

# Train Data
X_train = TrainData.iloc[:,[0,1,2]].values # Features Data
Y_train = TrainData.iloc[:,[3]].values     # Labeled Data

# Test Data
X_test = TestData.iloc[:,[0,1,2]].values
Y_test = TestData.iloc[:,[3]].values

# Show Train Data
X_train,Y_train

# Show Test Data
X_test,Y_test

### Define Error Metrics
#### As this is a regression problem, we have defined MAPE as the error metrics as shown below


def MAPE(Y_actual,Y_Predicted):
    Mape = np.mean(np.abs((Y_actual - Y_Predicted)/Y_actual))*100
    return Mape

## Build the Model of KNN Classification

#Building the KNN.Regressor Model on our dataset
k=3
from sklearn.neighbors import KNeighborsClassifier
KNN_model = KNeighborsClassifier(n_neighbors=k,metric='euclidean') # euclidean & minkowski & manhattan & 
KNN_model.fit(X_train,Y_train.ravel())

# The following lists the string metric identifiers and the associated distance metric classes:

# Metrics intended for real-valued vector spaces:

#### “euclidean”  = > sqrt(sum((x - y)^2))

#### “manhattan” => sum(|x - y|)

#### “chebyshev” => max(|x - y|)

#### “minkowski” => sum(|x - y|^p)^(1/p)

#### “wminkowski” => sum(|w * (x - y)|^p)^(1/p)

#### “seuclidean” => sqrt(sum((x - y)^2 / V))

#### “mahalanobis” => sqrt((x - y)' V^-1 (x - y))

### Predict the testing Data


KNN_predict = KNN_model.predict(X_test)  # Predictions on Testing data

X_test

Y_test = KNN_predict # Set Predicted label put on Y_Test
Y_test   # Predicted Values

## Accuracy Check For KNN Classification !

# Using MAPE error metrics to check for the error rate and accuracy level
KNN_MAPE = MAPE(Y_train,KNN_predict)
Accuracy_KNN = 100 - KNN_MAPE
print("MAPE: ",KNN_MAPE)
print('Accuracy of KNN model: {:0.2f}%.'.format(Accuracy_KNN))

## Build the Model of KNN Regressor Classification

#Building the KNN.Regressor Model on our dataset
k=3
from sklearn.neighbors import KNeighborsRegressor
KNN_model = KNeighborsRegressor(n_neighbors=k).fit(X_train,Y_train)

### Predict the testing Data

KNN_predict = KNN_model.predict(X_test) #Predictions on Testing data

X_test

Y_test = KNN_predict # Set Predicted label put on Y_Test
Y_test   # Predicted Values

## Accuracy Check For KNN Regressor Classification!

# Using MAPE error metrics to check for the error rate and accuracy level
KNN_MAPE = MAPE(Y_train.reshape(1, -1),KNN_predict)
Accuracy_KNN = 100 - KNN_MAPE
print("MAPE: ",KNN_MAPE)
print('Accuracy of KNN model: {:0.2f}%.'.format(Accuracy_KNN))