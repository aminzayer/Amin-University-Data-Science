# K-means Practice 
# Data x1=(1   1   4),x2=(2   2   1),x3=(7   5   6),x4=(6   5   5),x5=(1   0   2),x6=(9   8   7),x6=(4   5   7),x7=(2   1   2)
# 3D => 3 Dimention Data
# Amin Zayeromali  ==> amin.zayeromali@gmail.com  Likedin Profile : https://ir.linkedin.com/in/aminzayeromali

# Import Python Library
import pandas as pd
from sklearn.cluster import KMeans
from matplotlib import pyplot as plt

# Use Pandas lib for Create Dataframe
MyData = pd.DataFrame(
    [[1, 1, 4],
     [2, 2, 1],
     [7, 5, 6],
     [6, 5, 5],
     [1, 0, 2],
     [9, 8, 7],
     [4, 5, 7],
     [2, 1, 2]], columns=['F1', 'F2', 'F3'])

# Use Matplotlib For plotting data  
# plot 3D Data
fig = plt.figure()
ax = plt.axes(projection='3d')
ax = plt.axes(projection='3d')
ax.scatter3D(MyData['F1'], MyData['F2'], MyData['F3'])

# Use K-Means Alogrithm from Sklearn Lib
K = 2  # Number of Clusters
km = KMeans(K)  
clusts = km.fit_predict(MyData)

# Add Clusters Label to DataFrame
MyData['clusts'] = clusts
print(MyData)

# Use Matplotlib For plotting Clustered data
fig = plt.figure()
ax = plt.axes(projection='3d')
ax = plt.axes(projection='3d')
ax.scatter3D(MyData['F1'], MyData['F2'], MyData['F3'], c=MyData['clusts'])
