# loading up the libraries
import pandas as pd
import numpy as np
import random as rd
#import matplotlib.pyplot as plt


def k_means_fit(X, centroids, n=5):
    #get a copy of the original data
    X_data = X

    diff = 1
    j = 0

    while(diff != 0):

        #creating a copy of the original dataframe
        i = 1

        #iterate over each centroid point
        for index1, row_c in centroids.iterrows():
            ED = []

            #iterate over each data point
            for index2, row_d in X_data.iterrows():

                #calculate distance between current point and centroid
                d1 = abs(row_c["F1"]-row_d["F1"])
                d2 = abs(row_c["F2"]-row_d["F2"])
                d3 = abs(row_c["F3"]-row_d["F3"])
                d = d1+d2+d3

                #append distance in a list 'ED'
                ED.append(d)
                #print("X (F1=", row_c["F1"], ",F2=", row_c["F2"],") <=> "," X (F1=", row_d["F1"],",F2=", row_d["F2"],") = ",d1, " + ", d2, " => D = ", d)

            #append distace for a centroid in original data frame
            X[i] = ED
            i = i+1
        
        print("\n", X)
        C = []
        for index, row in X.iterrows():

            #get distance from centroid of current data point
            min_dist = row[1]
            pos = 1

            #loop to locate the closest centroid to current point
            for i in range(n):

                #if current distance is greater than that of other centroids
                if row[i+1] < min_dist:

                    #the smaller distanc becomes the minimum distance
                    min_dist = row[i+1]
                    pos = i+1
            C.append(pos)

        #assigning the closest cluster to each data point
        X["Cluster"] = C

        #grouping each cluster by their mean value to create new centroids
        centroids_new = X.groupby(["Cluster"]).mean()[["F3", "F2", "F1"]]
        print("centroids =\n", centroids, "\nNew centroids = \n", centroids_new)
        if j == 0:
            diff = 1
            j = j+1

        else:
            #check if there is a difference between old and new centroids
            diff = (centroids_new['F3'] - centroids['F3']).sum() + (centroids_new['F2'] -
                                                                 centroids['F2']).sum() + (centroids_new['F1'] - centroids['F1']).sum()
            print("-------- End Algorithms ---------------", diff.sum(), "\n")

        centroids = X.groupby(["Cluster"]).mean()[["F3", "F2", "F1"]]

    return X, centroids


# data = pd.DataFrame([[3, 5, 6],
#                      [2, 7, 5],
#                      [2, 1, 1],
#                      [1, 0, 1],
#                      [5, 9, 7],
#                      [6, 8, 8],
#                      [1, 0, 2],
#                      [4, 4, 4],
#                      [2, 2, 2],
#                      [9, 9, 9]],
#                     columns=['F1', 'F2', 'F3'])



# #centroids = get_random_centroids(data, k=2)
# # Set Manual centroids
# centroids = pd.DataFrame([[1, 0, 1],
#                           [5, 9, 7],
#                           [2, 7, 5]],
#                          columns=['F1', 'F2', 'F3'])
# # print(centroids)
# clustered, cent = k_means_fit(data, centroids, n=3)
# print(cent)
# print(clustered)


data = pd.DataFrame([[1, 3, 5],
                     [6, 7, 2],
                     [5, 8, 4],
                     [3, 3, 4],
                     [8, 7, 1],
                     [9, 7, 2],
                     [4, 3, 4],
                     [1, 2, 1],
                     [3, 7, 2]],
                    columns=['F1', 'F2', 'F3'])


#centroids = get_random_centroids(data, k=2)
# Set Manual centroids
centroids = pd.DataFrame([[1, 3, 5],
                          [6, 7, 2]],
                         columns=['F1', 'F2', 'F3'])
# print(centroids)
clustered, cent = k_means_fit(data, centroids, n=2)
print(cent)
print(clustered)
