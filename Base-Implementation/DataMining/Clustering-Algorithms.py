#loading up the libraries
import pandas as pd
import numpy as np
import random as rd
#import matplotlib.pyplot as plt

data = pd.DataFrame([[3, 4],
                     [5, 6],
                     [1, 1],
                     [2, 1],
                     [7, 5],
                     [0, 2],
                     [5, 6]],
                    columns=['F1', 'F2'])


def get_random_centroids(X, k=3):
    #return random samples from the dataset
    cent = (X.sample(n=k))
    return cent


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
                # d1 = (row_c["F1"]-row_d["F1"])**2
                # d2 = (row_c["F2"]-row_d["F2"])**2
                # d = np.sqrt(d1+d2)
                d1 = abs(row_c["F1"]-row_d["F1"])
                d2 = abs(row_c["F2"]-row_d["F2"])
                d = d1+d2

                #append distance in a list 'ED'
                ED.append(d)
                #print("X (F1=", row_c["F1"], ",F2=", row_c["F2"],") <=> "," X (F1=", row_d["F1"],",F2=", row_d["F2"],") = ",d1, " + ", d2, " => D = ", d)

            #append distace for a centroid in original data frame
            X[i] = ED
            i = i+1
            print("\n",X)

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
        centroids_new = X.groupby(["Cluster"]).mean()[["F2", "F1"]]
        print("centroids =\n", centroids, "\nNew centroids = \n", centroids_new)
        if j == 0:
            diff = 1
            j = j+1
        
        else:
            #check if there is a difference between old and new centroids
            diff = (centroids_new['F2'] - centroids['F2']).sum() + \
                (centroids_new['F1'] - centroids['F1']).sum()
            print("-------- End Algorithms ---------------",diff.sum(),"\n")

        centroids = X.groupby(["Cluster"]).mean()[["F2", "F1"]]

    return X, centroids


#centroids = get_random_centroids(data, k=2)
# Set Manual centroids
centroids = pd.DataFrame([[1, 1],
                          [7, 5]],
                          columns=['F1', 'F2'])
#print(centroids)
clustered, cent = k_means_fit(data, centroids, n=2)
print(cent)
print(clustered)


# #setting color values for our
# color = ['brown', 'blue', 'green', 'cyan']

# #plot data
# for k in range(len(color)):
#     cluster = clustered[clustered["Cluster"] == k+1]
#     plt.scatter(cluster["F1"], cluster["F2"], c=color[k])

# #plot centroids
# plt.scatter(cent["F1"], cent["F2"], c='red')
# plt.xlabel('Height/ cm')
# plt.ylabel('Weight/ kg')
